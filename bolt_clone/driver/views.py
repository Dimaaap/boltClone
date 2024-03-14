import json
import base64
from uuid import uuid4

import pyshorteners
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.core.files.base import ContentFile
from django.core.exceptions import FieldDoesNotExist

from twilio.rest import Client

from .db_services import get_all_data_from_model, filter_data_from_model
from .form_handlers import driver_registration_form_handler, send_sms_message_service, verification_first_step
from .forms import (DriverRegistrationForm, PhoneNumberVerificationForm, DriverCarInfoForm, DriverCarDocumentsForm)
from .services import *
from .models import DriverCarDocuments, Driver, DriverCarInfo

data_storage = DataStorage()
client = Client(data_storage.ACCOUNT_SID, data_storage.AUTH_TOKEN)


def driver_main_page(request):
    if check_if_device_unique(request):
        is_verification = True
    else:
        is_verification = False
    if request.method == "POST":
        form = DriverRegistrationForm(request.POST)
        if form.is_valid():
            user_token = driver_registration_form_handler(request, form)
            if user_token:
                return redirect(verification_phone_number, user_token)
            else:
                messages.error(request, "Здається, щось пішло не так")
        else:
            print(form.errors)
    else:
        form = DriverRegistrationForm(initial={"driver_city": "Київ"})
    countries_list = form_dropdown_cities_window()
    user_email = request.session.get("email", "")
    last_user_page = get_user_last_registration_page(request)
    context = {"form": form, "countries_list": countries_list, "verification": is_verification,
               "user_email": user_email, "last_page": last_user_page}
    return render(request, "driver/main_page.html", context)


def verification_phone_number(request, verification_code):
    if not check_if_token_verified(request, verification_code):
        return redirect(driver_main_page)
    if request.method == "POST":
        form = PhoneNumberVerificationForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data["otp_code"]
            sent_code = request.session["otp_code"]
            if int(code) == int(sent_code):
                new_user = {"email": request.session["email"],
                            "phone_number": request.session["phone_number"],
                            "city": request.session["city"]}
                client_ip = get_client_ip(request)
                driver_city = get_data_from_model(DriverCities, "city_title", new_user["city"])
                new_driver = Driver(driver_email=new_user["email"],
                                    driver_phone_number=new_user["phone_number"],
                                    driver_city=driver_city,
                                    device_id=client_ip,
                                    is_verification=True)
                try:
                    new_driver.objects.get_or_create()
                except Exception as e:
                    messages.error(request, "Здається, щось пішло не так")
            else:
                form.add_error("otp_code", "Неправильний код.Надіслати код ще раз")
        else:
            messages.error(request, "Неправильний код. Спробуйте ще раз")
    else:
        form = PhoneNumberVerificationForm()
    user_phone_number = request.session.get("new_user")["phone_number"]
    context = {"form": form, "phone_number": user_phone_number}
    return render(request, "driver/verification_page.html", context)


def resend_code_view(request):
    user_phone_number = request.session["user_phone_number"]
    verification_code = request.session["verification_code"]
    send_sms_message_service(client, request, user_phone_number)
    return redirect(verification_phone_number, verification_code)


def registration_first_page(request, device_ip: str):
    request.session["on_first_page"] = True
    if request.method == "POST":
        form = DriverCarInfoForm(request.POST)
        if form.is_valid():
            verification_first_step(request, form)
            return redirect(registration_second_page, device_ip)
        else:
            print(form.errors)
    else:
        form = DriverCarInfoForm()
    cars_list = get_all_data_from_model(DriverCars)
    year_list = [int(year) for year, _ in data_storage.CAR_CREATED_YEAR_LIST]
    car_color_list = [color for color, _ in data_storage.CAR_COLORS_LIST]
    request.session["device_ip"] = device_ip
    context = {"form": form, "cars": cars_list, "year_list": year_list, "color_list": car_color_list}
    return render(request, "driver/registration_first_page.html", context)


def registration_second_page(request, device_ip):
    request.session["on_second_page"] = True
    try:
        del request.session["on_first_page"]
    except KeyError:
        pass
    if request.method == "POST":
        form = DriverCarDocumentsForm(request.POST)
    else:
        form = DriverCarDocumentsForm()
    context = {"form": form, "device_ip": device_ip}
    return render(request, "driver/registration_second_page.html", context)


def create_random_file_name_service() -> str:
    file_name = uuid4()
    return str(file_name)


def decoded_request_body_service(file_url: str) -> ContentFile:
    image_format, image_str = file_url.split(";base64,")
    image_extension = image_format.split('/')[-1]
    data = base64.b64decode(image_str)
    file_name = create_random_file_name_service()
    image_file = ContentFile(data, name=f"f{file_name}.{image_extension}")
    return image_file

def shorten_image_url(image_url: str) -> str:
    s = pyshorteners.Shortener()
    shorten_url = s.chilpit.short(image_url)
    return shorten_url


def save_file_in_model_service(request, field_name: str, exp_time: str, file_url: str):
    image_file = decoded_request_body_service(file_url)
    current_driver = get_driver_by_email_service(request)
    driver_car_info = get_driver_car_info_by_driver_service(current_driver)
    driver_docs = get_data_from_model(DriverCarDocuments, "driver_car_id", driver_car_info)
    file_url = shorten_image_url(file_url)
    try:
        image_model_field = DriverCarDocuments._meta.get_field(field_name)
    except FieldDoesNotExist:
        print("Field does not exist")
    else:
        if field_name != "driver_photo":
            image_expiration_date = DriverCarDocuments._meta.get_field(f"{field_name}_expiration_time")
            if not driver_docs:
                new_car_doc = DriverCarDocuments()
                setattr(new_car_doc, image_model_field.name, file_url)
                setattr(new_car_doc, image_expiration_date.name, exp_time)
                new_car_doc.driver_car_id = driver_car_info
                new_car_doc.save()
                print("In new_car_doc container")
            else:
                setattr(driver_docs, image_model_field.name, file_url)
                setattr(driver_docs, image_expiration_date.name, exp_time)
                driver_docs.save()
                print("In driver_docs container")
        else:
            if not driver_docs:
                new_car = DriverCarDocuments.objects.create(driver_car_id=driver_car_info, driver_photo=file_url)
                print("In not driver_docs container")
                new_car.save()
        print("dsadsadsa")



def get_driver_by_email_service(request):
    driver_email = request.session.get("email")
    driver = get_data_from_model(Driver, "driver_email", driver_email)
    return driver


def get_driver_car_info_by_driver_service(driver):
    driver_car_info = get_data_from_model(DriverCarInfo, "driver_id", driver)
    return driver_car_info


@csrf_exempt  # TODO: REMOVE IT BEFORE DEPLOY
def save_file_view(request, field_name: str, exp_time: str):
    if request.method == "POST":
        file = request.POST.get("file")
        image_file = save_file_in_model_service(request, field_name, exp_time, file)
    return JsonResponse({"message": "File saved success", "status": "success"})


@csrf_exempt  # TODO: REMOVE IT BEFORE DEPLOY
def search_car_models(request, device_ip):
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        term = data.get("term", "")
        car_list = DriverCars.objects.filter(model_title__icontains=term).values("model_title")
        return JsonResponse(list(car_list), safe=False)
    else:
        return JsonResponse({"error": "Метод не підтримується"}, status=405)


@csrf_exempt  # TODO: REMOVE IT BEFORE DEPLOY
def search_car_models_by_car(request, device_ip, brand):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))
            brand = data["brand"]
            car = get_data_from_model(DriverCars, "model_title", brand)
            models = filter_data_from_model(DriverCarModels, "car_id", car.model_id).values_list("model", flat=True)
            return JsonResponse(list(models), safe=False)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
