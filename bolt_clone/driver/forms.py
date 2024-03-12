import re

from django import forms
from django.core.exceptions import ObjectDoesNotExist
from phonenumber_field.formfields import PhoneNumberField

from .data_storage import DataStorage
from .models import Driver

data_storage = DataStorage()

CAR_COLOR_CHOICES = [("", "")] + data_storage.CAR_COLORS_LIST
CAR_YEAR_CHOICES = [("", "")] + data_storage.CAR_CREATED_YEAR_LIST


class DriverRegistrationForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(DriverRegistrationForm, self).__init__(*args, **kwargs)
        self.fields["driver_city"].empty_label = None

    driver_email = forms.EmailField(label="Адреса електронної пошти", required=True,
                                    widget=forms.EmailInput(attrs={
                                        "class": "form-control",
                                        "id": "driver-email",
                                        "placeholder": "Введіть адресу електронної пошти"
                                    }))

    driver_phone_number = PhoneNumberField(region="UA", label="Номер телефону",
                                           widget=forms.NumberInput(attrs={
                                               "class": "form-control",
                                               "id": "driver-number",
                                               "placeholder": "Номер мобільного телефону"
                                           }))
    driver_phone_number.error_messages["invalid"] = "Некоректний формат номеру(+380501234123)"

    driver_city = forms.CharField(label="Місто",
                                  widget=forms.TextInput(attrs={
                                      "class": "form-control",
                                      "placeholder": "Місто, в якому ви будете їздити",
                                      "id": "city-select-field"
                                  }))

    driver_is_agree_with_policy = forms.BooleanField(
        required=True,
        widget=forms.CheckboxInput(attrs={"class": "agree-checkbox"})
    )

    def clean_driver_email(self):
        print("In validate method")
        driver_email = self.cleaned_data["driver_email"]
        try:
            Driver.objects.get(driver_email=driver_email)
        except ObjectDoesNotExist:
            return driver_email
        raise forms.ValidationError("Користувач з таким email уже зареєстрований на сайті")


class PhoneNumberVerificationForm(forms.Form):
    otp_code = forms.CharField(max_length=4, label="", required=True,
                               widget=forms.TextInput(attrs={"class": "form-control",
                                                             "id": "otp_code_field"}))


class DriverCarInfoForm(forms.Form):
    first_name = forms.CharField(max_length=100, label="Ім'я", required=True,
                                 widget=forms.TextInput(attrs={"class": "form-control",
                                                               "id": "driver-first-name-input-field",
                                                               "placeholder": "Ім'я"}))
    last_name = forms.CharField(max_length=100, label="Прізвище", required=True,
                                widget=forms.TextInput(attrs={"class": "form-control",
                                                              "id": "driver-last-name-input-field",
                                                              "placeholder": "Прізвище"}))
    referral_code = forms.CharField(max_length=20, label="Реферальний код(латиницею)", required=False,
                                    widget=forms.TextInput(attrs={"class": "form-control",
                                                                  "id": "driver-referral-code",
                                                                  "placeholder": "Реферальний код вводити тут"}))
    has_own_car = forms.BooleanField(required=False, label="У мене є авто, яке я водитиму",
                                     widget=forms.CheckboxInput(attrs={"checked": "checked"}))
    no_has_own_car = forms.BooleanField(required=False, label="Я бажаю знайти автопарк задля працевлаштування. "
                                                              "Натискаючи галочку, "
                                                              "Ви погоджуєтесь, що надана інформація про вас буде "
                                                              "передана автопаркам, що з нами співпрацюють, для "
                                                              "зв'язку та обговорення співпраці між Вами. Ви можете"
                                                              " скасувати свою згоду в будь-який час ",
                                        widget=forms.CheckboxInput(attrs={"checked": "checked"}))
    driver_car = forms.CharField(required=True, label="Марка(назва виробника) та модель авто",
                                 widget=forms.TextInput(attrs={
                                     "class": "form-control after-checkboxes with-span",
                                     "id": "driver-car-select"
                                 }))
    driver_car_model = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={
        "class": "form-control after-checkboxes hidden-field with-span",
        "id": "driver-model-car-select"
    }))
    created_year = forms.CharField(required=True, label="Рік випуску авто",
                                   widget=forms.TextInput(attrs={
                                       "class": "form-control after-checkboxes with-span",
                                       "id": "created-car-year-select-field",
                                       "readonly": "readonly"
                                   }))
    driver_number_sign = forms.CharField(required=True, label="Номерний знак",
                                         widget=forms.TextInput(attrs={
                                             "class": "form-control after-checkboxes",
                                             "id": "driver-number-sign",
                                             "placeholder": "AA7771AA"
                                         }))
    car_color = forms.CharField(required=True, label="Колір кузова авто",
                                widget=forms.TextInput(attrs={
                                    "class": "form-control after-checkboxes with-span",
                                    "id": "form-car-color-select-field",
                                    "readonly": "readonly"
                                }))

    def clean_driver_number_sign(self):
        driver_number_sign = self.cleaned_data["driver_number_sign"]
        ukrainian_pattern = r'^([АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ]{2}\s\d{4}\s[АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ]{2})'
        eu_pattern = r'([A-Z]{1,2}\d{4}\s?[A-Z]{0,2})|(\d{1,4}\s?[A-Z]{2,4})$'
        if not(re.match(ukrainian_pattern, driver_number_sign) or re.match(eu_pattern, driver_number_sign)):
            raise forms.ValidationError("Некоректний формат номеру телефону")
        if len(driver_number_sign) > 8:
            raise forms.ValidationError("Некоректний формат номеру")
        return driver_number_sign


class DriverCarDocumentsForm(forms.Form):
    driver_license = forms.FileField(required=True, label="Водійське посвідчення",
                                     widget=forms.FileInput(attrs={
                                         "class": "file-field-input",
                                         "id": "driver-licence",
                                         "accept": "image/*, application/pdf"
                                     }))
    driver_photo = forms.ImageField(required=True, label="Ваше фото",
                                    widget=forms.FileInput(attrs={
                                        "class": "file-field-input",
                                        "id": "driver-photo",
                                        "accept": "image/*"
                                    }))
    driver_tech_passport = forms.FileField(required=True, label="Техпаспорт",
                                           widget=forms.FileInput(attrs={
                                               "class": "file-field-input",
                                               "id": "driver-tech-passport",
                                               "accept": "image/*, application/pdf"
                                           }))
    driver_insurance_policy = forms.FileField(required=True, label="Страховий поліс авто",
                                              widget=forms.FileInput(attrs={
                                                  "class": "file-field-input",
                                                  "id": "driver-insurance-policy",
                                                  "accept": "image/*, application/pdf"
                                              }))