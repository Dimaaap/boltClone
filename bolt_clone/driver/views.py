from django.shortcuts import render, redirect
from django.contrib import messages

from twilio.rest import Client

from .forms import DriverRegistrationForm, PhoneNumberVerificationForm
from .services import form_dropdown_cities_window, get_client_ip
from .models import Driver
from .form_handlers import driver_registration_form_handler, send_sms_message_service
from .data_storage import DataStorage
from .db_services import get_data_from_model

data_storage = DataStorage()
client = Client(data_storage.ACCOUNT_SID, data_storage.AUTH_TOKEN)


def driver_main_page(request):
    driver_ip = get_client_ip(request)
    driver = get_data_from_model(Driver, "device_id", driver_ip)
    if driver and driver.is_verification:
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
    context = {"form": form, "countries_list": countries_list, "verification": is_verification}
    return render(request, "driver/main_page.html", context)


def verification_phone_number(request, verification_code):
    driver = Driver.verify_sms_code_token(verification_code)
    current_driver = get_data_from_model(Driver, "driver_email", request.session["user_email"])
    request.session["verification_code"] = verification_code
    if not driver:
        return redirect(driver_main_page)
    if request.method == "POST":
        form = PhoneNumberVerificationForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data["otp_code"]
            sent_code = request.session["otp_code"]
            if int(code) == int(sent_code):
                current_driver.verificate_user()
            else:
                form.add_error("otp_code", "Неправильний код.Надіслати код ще раз")
        else:
            messages.error(request, "Неправильний код. Спробуйте ще раз")
    else:
        form = PhoneNumberVerificationForm()
    user_phone_number = request.session["user_phone_number"]
    context = {"form": form, "phone_number": user_phone_number}
    return render(request, "driver/verification_page.html", context)


def resend_code_view(request):
    user_phone_number = request.session["user_phone_number"]
    verification_code = request.session["verification_code"]
    send_sms_message_service(client, request, user_phone_number)
    return redirect(verification_phone_number, verification_code)
