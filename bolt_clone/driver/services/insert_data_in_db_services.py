from bolt_clone.driver.services.services import get_data_from_model
from ..models import *

data_storage = DataStorage()


class InsertDataInDb:
    @staticmethod
    def insert_country_zones_in_db():
        try:
            for country_zone in data_storage.COUNTRY_ZONES_LIST:
                new_zone = CountryZones(zone_title=country_zone)
                new_zone.save()
        except Exception as e:
            print(e)

    @staticmethod
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

    @staticmethod
    def insert_cities_in_db():
        try:
            for country in data_storage.CITIES_LIST.keys():
                country_title = DriverCountries.objects.get(country_title=country)
                for city in data_storage.CITIES_LIST[country]:
                    new_city = DriverCities(city_title=city, country=country_title)
                    new_city.save()
        except Exception as e:
            print(e)

    @staticmethod
    def insert_cars_in_db():
        try:
            for model in data_storage.CAR_MODELS:
                new_car = DriverCars.objects.create(model_title=model)
                new_car.save()
        except Exception as e:
            print(e)

    @staticmethod
    def insert_car_models_in_db():
        try:
            for car in data_storage.MODELS_LIST:
                model_title = ''.join(car.keys())
                car_model = get_data_from_model(DriverCars, "model_title", model_title)
                for models in car.values():
                    for model in models:
                        new_model = DriverCarModels.objects.create(car_id=car_model, model=model)
                        new_model.save()
        except Exception as e:
            print(e)