from django.core.exceptions import ObjectDoesNotExist
from ip2geotools.databases.noncommercial import DbIpCity

from .models import CountryCode, CuisineCategory
from .data_storage import DataStorage

data_storage = DataStorage()


def get_form_select_initial_values_service(country_code):
    try:
        default_value = CountryCode.objects.get(country_code=country_code)
    except ObjectDoesNotExist:
        default_value = None
    return default_value


def get_user_country_by_ip_service(user_ip: str):
    response = DbIpCity.get(user_ip, api_key='free')
    if not response.country or response.country == 'ZZ':
        return get_form_select_initial_values_service("UA").pk
    else:
        return get_form_select_initial_values_service(response.country).pk


def insert_data_in_cuisines_model():
    cuisines = DataStorage.CUISINES_CHOICE
    counter = 1
    try:
        for _, i in cuisines:
            category = CuisineCategory()
            category.category_id = counter
            category.category_title = i
            category.save()
            counter += 1
    except Exception as e:
        print(e)