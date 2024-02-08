from .models import CountryZones, DriverCountries, DriverCities
from .data_storage import DataStorage

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