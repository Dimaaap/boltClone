from uuid import uuid4

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.hashers import make_password, check_password

from phonenumber_field.modelfields import PhoneNumberField

from .manager import OwnerManager
from .data_storage import DataStorage

data_storage = DataStorage()

class BusinessCountries(models.Model):
    country_id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    country_title = models.CharField(max_length=100, blank=True, default="")
    country_emoji = models.CharField(max_length=20, blank=True, default="")

    def __str__(self):
        return f"{self.country_emoji} {self.country_title}"

class BusinessOwnerData(AbstractBaseUser):
    username = None
    owner_id = models.CharField(primary_key=True, editable=False)
    email = models.CharField(max_length=60, unique=True)
    owner_first_name = models.CharField(max_length=100)
    owner_last_name = models.CharField(max_length=200)
    owner_phone_number = PhoneNumberField(region="UA")
    company_name = models.CharField(max_length=200)
    company_country_id = models.ForeignKey(BusinessCountries, on_delete=models.CASCADE)
    company_employees_count = models.CharField(max_length=14, blank=True)
    promo = models.CharField(max_length=50, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = OwnerManager()


    def __str__(self):
            return f"{self.owner_first_name} {self.owner_last_name} {self.company_name}"

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)