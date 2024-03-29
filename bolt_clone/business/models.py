from django.db import models

from uuid import uuid4


class BusinessOwnerData(models.Model):
    owner_id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    owner_email = models.CharField(max_length=60, unique=True)
    owner_password = models.CharField(max_length=200)


    def __str__(self):
        return f"{self.owner_id} - {self.owner_email}"