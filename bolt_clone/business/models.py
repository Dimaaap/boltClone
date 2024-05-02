from uuid import uuid4

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.hashers import make_password, check_password
from django.core.signing import TimestampSigner

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
    is_email_verified = models.BooleanField(default=False)
    is_legal_info_verified = models.BooleanField(default=False)
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

    def get_user_full_name(self):
        return f"{self.owner_first_name} {self.owner_last_name}"

    def generate_verification_token(self):
        signer = TimestampSigner()
        token = signer.sign(self.owner_id)
        return token



class CompanyLegalInformation(models.Model):
    company_legal_name = models.CharField(max_length=250, default="")
    bills_email = models.EmailField(max_length=150, default="")
    company_address = models.CharField(max_length=200, default="")
    edrpou_data = models.CharField(max_length=8, default="")
    company_ipn = models.CharField(max_length=12, default="")
    owner_id = models.ForeignKey(BusinessOwnerData, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.bills_email} {self.company_legal_name}"


class CompanySettingsInfo(models.Model):
    pdf_receipt_email = models.EmailField(max_length=150, default="")
    company_id = models.OneToOneField(CompanyLegalInformation, on_delete=models.CASCADE)
    company_codes = models.FileField(upload_to="codes/%Y/%m/%d")
    is_api_handle_allowed = models.BooleanField(default=False)
    promo_code = models.CharField(max_length=200, default="")


    def __str__(self):
        return f"{self.company_id} {self.pdf_receipt_email}"


class CompanyPolicies(models.Model):
    policy_id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    company_id = models.ForeignKey(CompanyLegalInformation, on_delete=models.CASCADE)
    policy_title = models.CharField(max_length=150, default="")
    policy_description = models.TextField(null=True, blank=True, default="")
    track_costs = models.CharField(max_length=11, choices=data_storage.TRACK_COSTS,
                                   default=data_storage.TRACK_COSTS[0])
    cost_level_track = models.CharField(max_length=16, choices=data_storage.COSTS_AMOUNT_CONTROL,
                                        default=data_storage.COSTS_AMOUNT_CONTROL[0])
    drive_day_and_time = models.CharField(max_length=13, choices=data_storage.DRIVE_AND_TIME_CHOICE,
                                          default=data_storage.DRIVE_AND_TIME_CHOICE[0])
    drive_places = models.CharField(max_length=25, choices=data_storage.DRIVE_PLACES,
                                    default=data_storage.DRIVE_PLACES[0])
    kind_service = models.CharField(max_length=100, default="")

    def __str__(self):
        return f"{self.policy_title} {self.policy_description}"


class TaxiLocation(models.Model):
    location_id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    policy_id = models.ForeignKey(CompanyPolicies, on_delete=models.CASCADE)
    location_title = models.CharField(max_length=200, default=""),
    location_address = models.CharField(max_length=255, default=""),
    radius = models.CharField(max_length=10, choices=data_storage.LOCATION_RADIUS,
                              default=data_storage.LOCATION_RADIUS[0])

    def __str__(self):
        return f"{self.location_title} {self.location_address}"
    

