from random import randint
import jwt
import datetime
from django.conf import settings

from twilio.base.exceptions import TwilioRestException

from .models import CountryZones, DriverCountries, DriverCities, Driver
from .data_storage import DataStorage
from .db_services import get_data_from_model

data_storage = DataStorage()


def insert_country_zones_in_db():
    try:
        for country_zone in data_storage.COUNTRY_ZONES_LIST:
            new_zone = CountryZones(zone_title=country_zone)
            new_zone.save()
    except Exception as e:
        print(e)


def insert_countries_in_db():
    try:
        for country in data_storage.COUNTRIES_LIST.keys():
            country_zone = CountryZones.objects.get(zone_title=country)
            for emoji, title in data_storage.COUNTRIES_LIST[country]:
                new_country = DriverCountries(country_title=title,
                                              country_emoji_flag=emoji,
                                              country_zone=country_zone)
                new_country.save()
    except Exception as e:
        print(e)


def insert_cities_in_db():
    try:
        for country in data_storage.CITIES_LIST.keys():
            country_title = DriverCountries.objects.get(country_title=country)
            for city in data_storage.CITIES_LIST[country]:
                new_city = DriverCities(city_title=city, country=country_title)
                new_city.save()
    except Exception as e:
        print(e)



def form_dropdown_cities_window():
    country_city_list = []
    for country in DriverCountries.objects.all():
        country_data = {
            "emoji": country.country_emoji_flag,
            "name": country.country_title,
            "cities": []
        }

        for city in DriverCities.objects.filter(country=country):
            country_data["cities"].append(city.city_title)
        country_city_list.append(country_data)
    sorted_country_list = sorted(country_city_list, key=lambda x: x["name"])
    sorted_country_list = sorted(sorted_country_list, key=lambda x: (x["name"] != "Україна", x["name"]))
    return sorted_country_list


def generate_sms_confirmation_code_service():
    code = randint(data_storage.SMALLEST_SMS_CODE_VALUE, data_storage.HIGHEST_SMS_CODE_VALUE)
    return code


def form_sms_message_service(client, generated_sms_code: str, user_phone_number):
    try:
        message = client.messages.create(
            body=f"\nЛаскаво просимо вас у Bolt Driver\n"
                 f"Ваш код для реєстрації - {generated_sms_code}\n"
                 f"Нікому не повідомляйте цей код",
            from_=data_storage.AUTH_TOKEN_PHONE_NUMBER,
            to=str(user_phone_number)
        )
    except TwilioRestException:
        print("exception")


def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip


def check_if_device_unique(request):
    driver_ip = get_client_ip(request)
    driver = get_data_from_model(Driver, "device_id", driver_ip)
    return driver and driver.is_verification


def generate_token(session_id):
    payload = {
        "session_id": session_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=600)
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
    return token


def verify_token(token, secret_key=settings.SECRET_KEY):
    try:
        decoded_payload = jwt.decode(token, secret_key, algorithms=["HS256"])
        return bool(decoded_payload)
    except jwt.ExpiredSignatureError:
        return "Token has expired"
    except jwt.InvalidTokenError:
        return "Invalid token"