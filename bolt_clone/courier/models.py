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
    courier_fleet = models.ForeignKey(FleetAddress, on_delete=models.CASCADE, null=True, default=None)

    def __str__(self):
        return f"{self.courier_first_name} {self.courier_last_name}"


class DeliveryMethod(models.Model):
    method_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    method_title = models.CharField(max_length=30, null=True, default="", blank=True)

    def __str__(self):
        return self.method_title


class CourierDocumentsInfo(models.Model):
    credit_card_name = models.CharField(max_length=150, null=False, blank=False)
    iban_number = models.CharField(max_length=40, null=False, blank=False)
    identification_number = models.CharField(max_length=11, null=False, blank=False)
    bank_card_certificate = models.ImageField(upload_to="documents/certificates", blank=False, default=False)
    document_image = models.ImageField(upload_to="documents/passports", blank=False, default=False)
    medicine_card_image = models.ImageField(upload_to="documents/medicine_cards", blank=False, default=False)
    courier_image = models.ImageField(upload_to="documents/photos", blank=False, default=False)
    delivery_method = models.ManyToManyField(DeliveryMethod)
    has_bag = models.BooleanField(default=False)
    courier = models.ForeignKey(CourierMainInfo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.credit_card_name} {self.courier}"
