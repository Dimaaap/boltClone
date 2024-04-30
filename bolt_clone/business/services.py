import re
import random
from string import ascii_letters

from django.core.exceptions import ObjectDoesNotExist
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.contrib.auth.hashers import check_password
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.conf import settings


from .filters import EqualFilter
from .data_storage import DataStorage
from .models import BusinessCountries, BusinessOwnerData
from driver.models import Driver
from courier.models import CourierMainInfo


data_storage = DataStorage()


def get_data_from_model(model, field: str, value: str):
    eq_filter = EqualFilter()
    try:
        field = model.objects.get(**eq_filter(field, value))
    except ObjectDoesNotExist:
        return False
    return field


def filter_data_from_model(model, field: str, value: str):
    eq_filter = EqualFilter()
    fields = model.objects.filter(**eq_filter(field, value))
    return fields


def insert_countries_in_db():
    countries = data_storage.COUNTRY_LIST
    for emoji, country_title in countries:
        new_country = BusinessCountries.objects.create(country_title=country_title, country_emoji=emoji)
        new_country.save()


def clear_session_service(request):
    session_keys = [i for i in request.session.keys() if not i.startswith("_")
                    and i != 'google-oauth2_state' and i != 'device_ip' and i != 'social_auth_last_login_backend']
    for i in session_keys:
        del request.session[i]


def search_country_in_model_service(company_country: str):
    company_country = company_country[2:].lstrip()
    country = get_data_from_model(BusinessCountries, "country_title", company_country)
    return country


def is_in_drivers_or_couriers_service(phone_number: str):
    driver = get_data_from_model(Driver, "driver_phone_number", phone_number)
    courier = filter_data_from_model(CourierMainInfo, "courier_phone_number", phone_number)
    return [driver, courier]


def validate_password_service(user_password: str):
    if all(i.isdigit() for i in user_password) or all(i.isalpha() for i in user_password):
        return False
    if len(user_password) < 6:
        return False
    return True


def check_input_username_service(first_name: str, last_name: str):
    if len(first_name) > 100 or len(last_name) > 200:
        return False
    return True


def send_user_mail(subject: str, user_email: str, file_name: str, user_token):
    html_message = render_to_string(f"business/emails/{file_name}", {"user_token": user_token})
    plain_message = strip_tags(html_message)
    from_email = settings.EMAIL_HOST_USER
    to = user_email
    send_mail(subject, plain_message, from_email, [to], html_message=html_message)


def compare_owner_passwords(old_password: str, owner_id):
    owner = get_data_from_model(BusinessOwnerData, "owner_id", owner_id)
    owner_password = owner.password
    return check_password(old_password, owner_password)


def check_user_email_service(user_email: str):
    try:
        validate_email(user_email)
    except ValidationError as e:
        return False
    return True


def check_user_phone_number_service(phone_number: str):
    return re.match(settings.NUMBER_PATTERN, phone_number)