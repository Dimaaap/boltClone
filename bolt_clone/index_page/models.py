import uuid
import requests

from django.db import models
from django.core.files.base import ContentFile
from phonenumber_field.modelfields import PhoneNumberField

from .data_storage import DataStorage

data_storage = DataStorage()


class CountryCode(models.Model):
    country_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    country_flag = models.ImageField(upload_to="flags/", blank=True, null=True)
    country_flag_image_url = models.URLField(blank=True, null=True)
    country_official_name = models.CharField(max_length=150)
    country_phone_code = models.CharField(max_length=20)
    country_native_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.country_flag} {self.country_native_name} ({self.country_phone_code})"

    def save_flag_image_from_url(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Error downloading image from {url}: {e}")
            return
        if response.status_code == 200:
            content_type = response.headers.get('content-type')
            if content_type.startswith("image"):
                self.country_flag.save(f"{self.country_official_name}.png", ContentFile(response.content), save=False)
                super().save()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.country_flag_image_url:
            self.save_flag_image_from_url(self.country_flag_image_url)


class BoltPartner(models.Model):
    partner_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    partner_name = models.CharField(max_length=255, null=False)
    partner_niche = models.CharField(max_length=65, choices=data_storage.NICHE_CHOICE,
                                     default='')
    is_restaurant = models.BooleanField(default=False)
    partner_cuisine = models.CharField(max_length=65,
                                       choices=data_storage.CUISINES_CHOICE, default='')
    partner_address = models.CharField(max_length=255, null=False),
    partner_postal_code = models.IntegerField(null=False),
    partner_email = models.EmailField(max_length=155, null=False)
    partner_phone = PhoneNumberField(blank=False, region="UA")
    is_agree_with_confidence = models.BooleanField(default=False)

    def __str__(self):
        return f'<{self.partner_name}> - {self.partner_id}'
