from .data_storage import DataStorage
from .models import City

data_storage = DataStorage()


def insert_cities_in_db(cities: list):
    for city in cities:
        City.objects.create(city_title=city)


def main():
    cities = data_storage.cities
    insert_cities_in_db(cities)