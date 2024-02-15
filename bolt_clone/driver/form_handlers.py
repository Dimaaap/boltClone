from django.shortcuts import redirect

from twilio.rest import Client

from .models import DriverCities, Driver
from .db_services import get_data_from_model
from .services import generate_sms_confirmation_code_service, form_sms_message_service, get_client_ip
from .data_storage import DataStorage
from .forms import DriverRegistrationForm

data_storage = DataStorage()
client = Client(data_storage.ACCOUNT_SID, data_storage.AUTH_TOKEN)


def driver_registration_form_handler(request, form):
    try:
        email, phone_number, city = (form.cleaned_data["driver_email"],
                                     form.cleaned_data["driver_phone_number"],
                                     form.cleaned_data["driver_city"])
        driver_city = get_data_from_model(DriverCities, "city_title", city)
        if not driver_city:
            return False
        device_id = get_client_ip(request)
        new_driver = Driver(driver_email=email, driver_phone_number=phone_number,
                            driver_city=driver_city, device_id=device_id)
        print(new_driver)
        new_driver.save()
        request.session["user_phone_number"] = str(phone_number)
        request.session["user_email"] = email
        user_token = new_driver.get_sms_code_token()
        request.session["generated_token"] = user_token
    except Exception as e:
        print(e)
        return redirect("number_verification")
    send_sms_message_service(client, request, phone_number)
    return user_token


def driver_save(driver):
    driver.save()


def send_sms_message_service(sms_client, request, phone_number):
    generated_sms_code = generate_sms_confirmation_code_service()
    request.session["otp_code"] = generated_sms_code
    form_sms_message_service(sms_client, generated_sms_code, phone_number)
