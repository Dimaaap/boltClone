import uuid

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from .data_storage import DataStorage

data_storage = DataStorage()


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
