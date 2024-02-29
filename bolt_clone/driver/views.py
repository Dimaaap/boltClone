import json

from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from twilio.rest import Client

from .forms import DriverRegistrationForm, PhoneNumberVerificationForm, DriverCarInfo
from .services import form_dropdown_cities_window, check_if_device_unique, verify_token, get_client_ip
from .models import Driver, DriverCities, DriverCars
from .form_handlers import driver_registration_form_handler, send_sms_message_service
from .data_storage import DataStorage
from .db_services import get_data_from_model, get_all_data_from_model

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
    context = {"form": form, "countries_list": countries_list, "verification": is_verification,
               "user_email": request.session["email"]}
    return render(request, "driver/main_page.html", context)


def verification_phone_number(request, verification_code):
    driver = verify_token(verification_code)
    request.session["verification_code"] = verification_code
    if isinstance(driver, str):
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
                new_driver.save()
            else:
                form.add_error("otp_code", "Неправильний код.Надіслати код ще раз")
        else:
            messages.error(request, "Неправильний код. Спробуйте ще раз")
    else:
        form = PhoneNumberVerificationForm()
    user_phone_number = request.session["user_phone_numer"]
    context = {"form": form, "phone_number": user_phone_number}
    return render(request, "driver/verification_page.html", context)


def resend_code_view(request):
    user_phone_number = request.session["user_phone_number"]
    verification_code = request.session["verification_code"]
    send_sms_message_service(client, request, user_phone_number)
    return redirect(verification_phone_number, verification_code)


def registration_first_page(request, device_ip: str):
    if request.method == "POST":
        form = DriverCarInfo(request.POST)
        if form.is_valid():
            pass
        else:
            pass
    else:
        form = DriverCarInfo()
    cars_list = get_all_data_from_model(DriverCars)
    context = {"form": form, "cars": cars_list}
    return render(request, "driver/registration_first_page.html", context)


@csrf_exempt  # TODO: REMOVE IT BEFORE DEPLOY
def search_car_models(request, device_ip):
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        term = data.get("term", "")
        print("Received term: " + term)
        car_list = DriverCars.objects.filter(model_title__icontains=term).values("model_title")
        print(list(car_list))
        return JsonResponse(list(car_list), safe=False)
    else:
        return JsonResponse({"error": "Метод не підтримується"}, status=405)


