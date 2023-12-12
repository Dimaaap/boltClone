import json

from django.conf import settings

from .models import CountryCode


def read_file():
    with open(settings.COUNTRIES_JSON_FILE, encoding="utf-8") as json_data:
        countries_dict = json.load(json_data)
    return countries_dict


def parse_countries_dict():
    countries_dict = read_file()
    res_list = [countries_dict[country] for country in countries_dict]
    return res_list


def sorted_countries_list():
    countries_list = parse_countries_dict()
    countries_list = sorted(countries_list, key=lambda obj: obj["title"])
    return countries_list


def get_select_window_list():
    countries_list = sorted_countries_list()
    select_list = []
    for country in countries_list:
        country_tuple = (country["flag"], country["title"], country["native_name"],
                         country["phone_code"], country["emoji_flag"],
                         country["country_code"])
        select_list.append(country_tuple)
    return select_list


def insert_countries_in_db():
    counter = 1
    countries = get_select_window_list()
    for country in countries:
        CountryCode.objects.create(
            country_id=counter,
            country_flag_image_url=country[0],
            country_official_name=country[1],
            country_emoji_flag=country[-2],
            country_phone_code=country[-3],
            country_native_name=country[-4],
            country_code=country[-1]
        )
        counter += 1
