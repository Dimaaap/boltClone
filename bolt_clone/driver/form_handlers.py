from django.shortcuts import redirect
from django.contrib import messages
from uuid import uuid4

from twilio.rest import Client

from .models import DriverCities, Driver, DriverCarModels, DriverCarInfo
from .db_services import get_data_from_model
from .services import generate_sms_confirmation_code_service, form_sms_message_service, generate_token
from .data_storage import DataStorage

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
        request.session["new_user"] = {
            "email": email,
            "phone_number": str(phone_number),
            "city": city
        }
        request.session["email"] = email
        request.session["phone_number"] = str(phone_number)
        request.session["city"] = city
        session_id = str(uuid4())
        user_token = generate_token(session_id)
        request.session["generated_token"] = user_token
    except Exception as e:
        return redirect("number_verification")
    send_sms_message_service(client, request, phone_number)
    return user_token


def send_sms_message_service(sms_client, request, phone_number):
    generated_sms_code = generate_sms_confirmation_code_service()
    request.session["otp_code"] = generated_sms_code
    form_sms_message_service(sms_client, generated_sms_code, phone_number)


def verification_first_step(request, form):
    (
        driver_first_name, driver_last_name, referral_code, driver_has_own_car, driver_no_has_own_car,
        driver_car, driver_car_model, driver_car_created_year, driver_number_sign, driver_car_color
    ) = form.cleaned_data.values()
    try:
        driver = get_data_from_model(Driver, "driver_email", request.session["email"])
        driver_car_model = get_data_from_model(DriverCarModels, "model", driver_car_model)
    except Exception:
        messages.error(request, "Щось пішло не так")
    else:
        new_driver_car_info, created = DriverCarInfo.objects.get_or_create(
            driver_id=driver,
            driver_first_name=driver_first_name.capitalize(),
            driver_last_name=driver_last_name.capitalize(),
            referral_code=referral_code,
            driver_has_own_car=driver_has_own_car,
            driver_car=driver_car_model,
            driver_number_sign=driver_number_sign.upper(),
            driver_car_color=driver_car_color
        )
        if created:
            new_driver_car_info.save()


