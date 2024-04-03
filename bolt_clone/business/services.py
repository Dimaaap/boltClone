from django.core.exceptions import ObjectDoesNotExist

from .filters import EqualFilter
from .data_storage import DataStorage
from .models import BusinessCountries


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


