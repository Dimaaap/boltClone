from random import randint

from django.shortcuts import render, redirect
from django.conf import settings
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

from .forms import DriverRegistrationForm, PhoneNumberVerificationForm
from .services import form_dropdown_cities_window
from .models import Driver, DriverCities


SMALLEST_SMS_CODE_VALUE = 1000
HIGHEST_SMS_CODE_VALUE = 9999
client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO.AUTH_TOKEN)


def generate_sms_confirmation_code():
    code = randint(SMALLEST_SMS_CODE_VALUE, HIGHEST_SMS_CODE_VALUE)
    return code


def driver_main_page(request):
    if request.method == "POST":
        form = DriverRegistrationForm(request.POST)
        if form.is_valid():
            email, phone_number, city = (form.cleaned_data["driver_email"], form.cleaned_data["driver_phone_number"],
                                         form.cleaned_data["driver_city"])
            driver_city = DriverCities.objects.get(city_title=city)
            new_driver = Driver(driver_email=email, driver_phone_number=phone_number,
                                driver_city=driver_city)
            new_driver.save()
            generated_sms_code = generate_sms_confirmation_code()
            request["user_phone_number"] = phone_number
            request["otp_code"] = generated_sms_code
            verification_code = "12321dqd"
            return redirect(verification_phone_number, verification_code)
        else:
            print(form.errors)
    else:
        form = DriverRegistrationForm(initial={"driver_city": "Київ"})
        print(form.fields)
    countries_list = form_dropdown_cities_window()
    context = {"form": form, "countries_list": countries_list}
    return render(request, "driver/main_page.html", context)


def verification_phone_number(request, verification_code):
    if request.method == "POST":
        form = PhoneNumberVerificationForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data["otp_code"]
            sent_code = request["otp_code"]
            if code == sent_code:
                print("equal")
        else:
            pass
    else:
        form = PhoneNumberVerificationForm()
    user_phone_number = request["user_phone_number"]
    context = {"form": form, "phone_number": user_phone_number}
    return render(request, "driver/verification_page.html", context)