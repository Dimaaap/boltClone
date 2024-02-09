from django import forms
from django.utils.html import format_html
from phonenumber_field.formfields import PhoneNumberField

from .models import DriverCities, DriverCountries
from .data_storage import DataStorage

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
