from django.db import transaction

from .models import CountryCode
from .sort_countries_list import get_select_window_list


def insert_countries_in_db():
    counter = 1
    countries = get_select_window_list()
    with transaction.atomic():
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
        country += 1

