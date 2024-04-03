from uuid import uuid4

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from .data_storage import DataStorage

data_storage = DataStorage()


class BusinessCountries(models.Model):
    country_id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    country_title = models.CharField(max_length=100, blank=True, default="")
    country_emoji = models.CharField(max_length=20, blank=True, default="")

    def __str__(self):
        return f"{self.country_emoji} {self.country_title}"

class BusinessOwnerData(models.Model):
    owner_id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    owner_email = models.CharField(max_length=60, unique=True)
    owner_password = models.CharField(max_length=200)
    owner_first_name = models.CharField(max_length=100)
    owner_last_name = models.CharField(max_length=200)
    owner_phone_number = PhoneNumberField(region="UA")
    company_name = models.CharField(max_length=200)
    company_country_id = models.ForeignKey(BusinessCountries, on_delete=models.CASCADE)
    company_employees_count = models.CharField(max_length=14, blank=True)
    promo = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.owner_first_name} {self.owner_last_name} {self.company_name}"