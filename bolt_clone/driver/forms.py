from django import forms
from django.core.exceptions import ObjectDoesNotExist
from phonenumber_field.formfields import PhoneNumberField

from .data_storage import DataStorage
from .models import Driver

data_storage = DataStorage()


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


class DriverCarInfo(forms.Form):
    first_name = forms.CharField(max_length=100, label="Ім'я", required=True,
                                 widget=forms.TextInput(attrs={"class": "form-control",
                                                               "id": "driver-first-name-input-field"}))
    last_name = forms.CharField(max_length=100, label="Прізвище")