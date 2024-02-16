from django.shortcuts import redirect
from uuid import uuid4

from twilio.rest import Client

from .models import DriverCities
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
