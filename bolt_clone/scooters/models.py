import uuid

from django.db import models

COMPANIES_CHOICES = [
    ("Bolt", "Bolt"),
    ("Bird", "Bird"),
    ("Lime", "Lime"),
    ("Tier", "Tier"),
    ("Voi", "Voi"),
    ("Wind", "Wind"),
    ("Інше", "Інше")
]


class ScooterReportModel(models.Model):
    report_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    scooter_img = models.ImageField(blank=False, null=True, upload_to="report/images")
    city = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=255, blank=True)
    rent_company = models.CharField(max_length=10, choices=COMPANIES_CHOICES)
    other_rent_company = models.CharField(max_length=50, default=None, null=True)
    scooter_id = models.CharField(max_length=10)
    problem_desc = models.TextField(default=None, null=True)

    def __str__(self):
        return f'{self.city} {self.address} {self.scooter_id}'