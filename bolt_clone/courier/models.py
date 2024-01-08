import uuid

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class City(models.Model):
    city_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    city_title = models.CharField(max_length=11, null=False)

    def __str__(self):
        return self.city_title


class FleetAddress(models.Model):
    address_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    address = models.CharField(max_length=155, null=True, default="")

    def __str__(self):
        return self.address


class CourierMainInfo(models.Model):
    courier_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    courier_first_name = models.CharField(null=False, max_length=140, blank=False)
    courier_last_name = models.CharField(null=False, max_length=180, blank=False)
    courier_phone_number = PhoneNumberField(blank=False)
    courier_email = models.EmailField(max_length=130, null=False, blank=False)
    courier_city = models.ForeignKey(City, on_delete=models.CASCADE)
    courier_fleet = models.ForeignKey(FleetAddress, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.courier_first_name} {self.courier_last_name}"
