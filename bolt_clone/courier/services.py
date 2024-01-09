from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django import forms

import logging

from .data_storage import DataStorage
from .db_services import get_field_from_model
from .models import City, CourierMainInfo, FleetAddress, DeliveryMethod

data_storage = DataStorage()
logger = logging.getLogger("main")


def insert_cities_in_db(cities: list):
    for city in cities:
        City.objects.create(city_title=city)


def insert_fleets_in_db(fleets: list):
    for fleet in fleets:
        FleetAddress.objects.create(address=fleet)


def insert_delivery_methods_in_db(methods: list):
    for method in methods:
        DeliveryMethod.objects.create(method_title=method)


def save_main_courier_form(request, form):
    (courier_first_name, courier_last_name, courier_phone_number,
     courier_email, courier_city, courier_fleet) = (form.cleaned_data["courier_first_name"],
                                                    form.cleaned_data["courier_last_name"],
                                                    form.cleaned_data["courier_phone_number"],
                                                    form.cleaned_data["courier_email"],
                                                    form.cleaned_data["courier_city"],
                                                    form.cleaned_data["courier_fleet"])
    try:
        if courier_city != "Київ":
            try:
                courier_fleet = get_field_from_model(FleetAddress, "address", courier_city)
            except ObjectDoesNotExist:
                logger.critical("UNEXPECTABLE ERROR!! courier_fleet don`t found")
        new_courier = CourierMainInfo.objects.create(courier_first_name=courier_first_name,
                                                     courier_last_name=courier_last_name,
                                                     courier_phone_number=courier_phone_number,
                                                     courier_email=courier_email, courier_city=courier_city,
                                                     courier_fleet=courier_fleet)
        new_courier.save()
    except Exception as e:
        print(e)
        messages.error(request, "Упс...Здається щось пішло не так, спробуйте,будь ласка надіслати форму ще раз")


def main():
    cities = data_storage.cities
    fleets = data_storage.fleets
    insert_cities_in_db(cities)
    insert_fleets_in_db(fleets)
