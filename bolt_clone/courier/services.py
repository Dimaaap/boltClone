from django.contrib import messages

from .data_storage import DataStorage
from .models import City, CourierMainInfo, FleetAddress

data_storage = DataStorage()


def insert_cities_in_db(cities: list):
    for city in cities:
        City.objects.create(city_title=city)


def insert_fleets_in_db(fleets: list):
    for fleet in fleets:
        FleetAddress.objects.create(address=fleet)


def save_main_courier_form(request, form):
    (courier_first_name, courier_last_name, courier_phone_number,
     courier_email, courier_city) = (form.cleaned_data["courier_first_name"],
                                     form.cleaned_data["courier_last_name"],
                                     form.cleaned_data["courier_phone_number"],
                                     form.cleaned_data["courier_email"],
                                     form.cleaned_data["courier_city"])
    try:
        new_courier = CourierMainInfo.objects.create(courier_first_name=courier_first_name,
                                                     courier_last_name=courier_last_name,
                                                     courier_phone_number=courier_phone_number,
                                                     courier_email=courier_email, courier_city=courier_city)
        new_courier.save()
    except Exception as e:
        print(e)
        messages.error(request, "Упс...Здається щось пішло не так, спробуйте,будь ласка надіслати форму ще раз")


def main():
    cities = data_storage.cities
    fleets = data_storage.fleets
    insert_cities_in_db(cities)
    insert_fleets_in_db(fleets)
