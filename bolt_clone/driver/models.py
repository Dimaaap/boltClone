from uuid import uuid4

from django.db import models

from .data_storage import DataStorage

from phonenumber_field.modelfields import PhoneNumberField

data_storage = DataStorage()


class CountryZones(models.Model):
    zone_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    zone_title = models.CharField(max_length=20)

    def __str__(self):
        return self.zone_title


class DriverCountries(models.Model):
    country_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    country_title = models.CharField(max_length=50, default="")
    country_emoji_flag = models.CharField(max_length=15, blank=True, default='')
    country_zone = models.ForeignKey(CountryZones, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.country_emoji_flag} {self.country_title}'


class DriverCities(models.Model):
    city_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    city_title = models.CharField(max_length=120, blank=True, default="")
    country = models.ForeignKey(DriverCountries, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.city_title}'


class Driver(models.Model):
    driver_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    driver_email = models.EmailField(unique=True, max_length=100)
    driver_phone_number = PhoneNumberField(blank=False)
    driver_city = models.ForeignKey(DriverCities, on_delete=models.CASCADE, default="")
    device_id = models.GenericIPAddressField(default="", null=True)
    is_verification = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.driver_email} {self.driver_phone_number}"


class DriverCars(models.Model):
    model_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    model_title = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.model_title}"


class DriverCarModels(models.Model):
    model_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    car_id = models.ForeignKey(DriverCars, on_delete=models.CASCADE)
    model = models.CharField(max_length=100)


class DriverCarInfo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    driver_id = models.ForeignKey(Driver, on_delete=models.CASCADE)
    driver_first_name = models.CharField(max_length=70)
    driver_last_name = models.CharField(max_length=80)
    referral_code = models.CharField(max_length=20, null=True, default="")
    driver_has_own_car = models.BooleanField(default=True)
    driver_car = models.ForeignKey(DriverCarModels, on_delete=models.CASCADE, default="")
    driver_car_created_year = models.CharField(max_length=4,
                                               choices=data_storage.CAR_CREATED_YEAR_LIST,
                                               null=True, blank=True)
    driver_number_sign = models.CharField(max_length=8, null=True, default="")
    driver_car_color = models.CharField(max_length=50, choices=data_storage.CAR_COLORS_LIST)

    def __str__(self):
        return f"{self.driver_first_name} {self.driver_last_name}"


class DriverCarDocuments(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    driver_car_id = models.ForeignKey(DriverCarInfo, on_delete=models.CASCADE)
    driver_license = models.FileField(upload_to="docs/license/%Y/%m/%d/", null=True, default=None, max_length=1000)
    driver_license_expiration_time = models.DateField(auto_now=False, null=True)
    driver_photo = models.FileField(upload_to="docs/photos/%Y/%m/%d/", null=True, default=None, max_length=1000)
    driver_tech_passport = models.FileField(upload_to="docs/tech_passports/%Y/%m/%d/",
                                            null=True, default=None, max_length=1000)
    driver_tech_passport_expiration_time = models.DateField(auto_now=False, null=True)
    driver_insurance_policy = models.FileField(upload_to="docs/insurance_policy/%Y/%m/%d/",
                                        null=True, default=None, max_length=1000)
    driver_insurance_policy_expiration_time = models.DateField(auto_now=False, null=True)

    def __str__(self):
        return (f"{self.driver_car_id} --- {self.driver_license} --- {self.driver_photo}"
                f"--- {self.driver_tech_passport} --- {self.driver_insurance_policy}")

    def is_file_uploaded(self, field_name):
        file_field = getattr(self, field_name)
        return bool(file_field)


    def check_uploaded_file(self):
        uploaded_files = []
        for field in self._meta.fields:
            if isinstance(field, (models.FileField, models.ImageField)):
                field_name = field.name
                if self.is_file_uploaded(field_name):
                    uploaded_files.append(field_name)
                else:
                    uploaded_files.append(None)
        return uploaded_files


    def get_model_field_values(self):
        files = {}
        for file in self.check_uploaded_file():
            if file:
                uploaded_file = getattr(self, file)
                files[file] = uploaded_file
        return files

    def get_field_value_by_title(self, field_name: str):
        return getattr(self, field_name)


    def get_files_expiration_time(self):
        files = self.get_model_field_values()
        files_exp_time = {}
        for file_name in files:
            if file_name != "driver_photo":
                file_name_exp_time_field = f"{file_name}_expiration_time"
                exp_time = getattr(self, file_name_exp_time_field)
                files_exp_time[file_name] = exp_time
        return files_exp_time
