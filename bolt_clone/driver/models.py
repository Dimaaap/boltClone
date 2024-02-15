from uuid import uuid4
from time import time
import jwt

from django.db import models
from django.conf import settings

from .db_services import get_data_from_model

from phonenumber_field.modelfields import PhoneNumberField


class CountryZones(models.Model):
    zone_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    zone_title = models.CharField(max_length=20)

    def __str__(self):
        return self.zone_title


class DriverCountries(models.Model):
    country_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    country_title = models.CharField(max_length=50, default="")
    country_emoji_flag = models.CharField(max_length=15, blank=True, default='')
    country_zone = models.ForeignKey(CountryZones, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.country_emoji_flag} {self.country_title}'


class DriverCities(models.Model):
    city_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    city_title = models.CharField(max_length=120, blank=True, default="")
    country = models.ForeignKey(DriverCountries, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.city_title}'


class Driver(models.Model):
    driver_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    driver_email = models.EmailField(unique=True, max_length=100)
    driver_phone_number = PhoneNumberField(blank=False)
    driver_city = models.ForeignKey(DriverCities, on_delete=models.CASCADE, default="")
    device_id = models.GenericIPAddressField(default="", null=True)
    is_verification = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.driver_email} {self.driver_phone_number}"

    def get_sms_code_token(self, expires_in=600):
        return jwt.encode(
            {"reset_page": str(self.driver_id), "exp": time() + expires_in},
            settings.SECRET_KEY, algorithm="HS256"
        )

    def verificate_user(self):
        self.is_verification = True

    @staticmethod
    def verify_sms_code_token(token):
        try:
            driver_id = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])["reset_page"]
        except Exception as e:
            return None
        return get_data_from_model(Driver, "driver_id", driver_id)

