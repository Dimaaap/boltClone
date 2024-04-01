from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

from uuid import uuid4


class BusinessOwnerData(models.Model):
    owner_id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    owner_email = models.CharField(max_length=60, unique=True)
    owner_password = models.CharField(max_length=200)


    def __str__(self):
        return f"{self.owner_id} - {self.owner_email}"


class BusinessOwnerPersonalData(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    owner_first_name = models.CharField(max_length=100)
    owner_last_name = models.CharField(max_length=150)
    owner_mobile_number = PhoneNumberField(blank=True)
    owner_id = models.OneToOneField(BusinessOwnerData, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.owner_first_name} {self.owner_last_name}"