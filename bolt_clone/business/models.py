from uuid import uuid4

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, UserManager
from phonenumber_field.modelfields import PhoneNumberField

from .data_storage import DataStorage

data_storage = DataStorage()


class DataOwnerManager(BaseUserManager):
    def create_user(self, owner_email, owner_first_name, owner_last_name, owner_phone_number,
                    company_name, company_country_id, company_employees_count, promo,
                    password=None, **extra_fields):
        if not owner_email:
            raise ValueError('The Email field must be set')
        owner_email = self.normalize_email(owner_email)
        user = self.model(owner_email=owner_email, owner_first_name=owner_first_name,
                          owner_last_name=owner_last_name, owner_phone_number=owner_phone_number,
                          company_name=company_name, company_country_id=company_country_id,
                          company_employees_count=company_employees_count, promo=promo, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, owner_email, owner_first_name, owner_last_name, owner_phone_number,
                         company_name, company_country_id, company_employees_count, promo,
                         password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')

        return self.create_user(owner_email, owner_first_name, owner_last_name, owner_phone_number,
                                company_name, company_country_id, company_employees_count, promo,
                                password, **extra_fields)



class BusinessCountries(models.Model):
    country_id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    country_title = models.CharField(max_length=100, blank=True, default="")
    country_emoji = models.CharField(max_length=20, blank=True, default="")

    def __str__(self):
        return f"{self.country_emoji} {self.country_title}"

class BusinessOwnerData(AbstractBaseUser):
    owner_id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    owner_email = models.CharField(max_length=60, unique=True)
    owner_first_name = models.CharField(max_length=100)
    owner_last_name = models.CharField(max_length=200)
    owner_phone_number = PhoneNumberField(region="UA")
    company_name = models.CharField(max_length=200)
    company_country_id = models.ForeignKey(BusinessCountries, on_delete=models.CASCADE)
    company_employees_count = models.CharField(max_length=14, blank=True)
    promo = models.CharField(max_length=50, blank=True)

    USERNAME_FIELD = "owner_email"
    REQUIRED_FIELDS = ["owner_first_name", "owner_last_name", "owner_phone_number", "company_name",
                       "company_country_id", "company_employees_count"]

    objects = DataOwnerManager()

    def __str__(self):
        return f"{self.owner_first_name} {self.owner_last_name} {self.company_name}"