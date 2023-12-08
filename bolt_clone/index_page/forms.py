from django import forms
from django.utils.html import format_html
from phonenumber_field.formfields import PhoneNumberField

from .models import BoltPartner, CountryCode
from .data_storage import DataStorage

data_storage = DataStorage()


class CountryFlagSelect(forms.widgets.Select):
    def create_option(
            self, name, value, label, selected, index, subindex=None, attrs=None
    ):
        option = super().create_option(name, value, label, selected, index, subindex, attrs)
        if "data-flag-url" in attrs:
            option["attrs"]["data-flag-url"] = attrs.get('data-flag-url', '')
        return option

    def format_value(self, value):
        country = next((c for c in self.choices if str(c[0]) == value), None)
        if country:
            country = country[1]
            return format_html("<img src='{}' width='20' height='20'>{}",
                               country.country_flag.url, country.country_native_name)
        return super().format_value(value)


class AddPartnerForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("label_suffix", "")
        super(AddPartnerForm, self).__init__(*args, **kwargs)
        self.fields["country_phone_code"].empty_label = None
        self.fields["country_phone_code"].widget = CountryFlagSelect(attrs={
            "class": "form-control select-country-flag"
        })

    class Meta:
        model = BoltPartner
        fields = ("partner_name", "partner_niche",
                  "partner_cuisine", "partner_address",
                  "partner_postal_code", "partner_email",
                  "partner_phone", "is_agree_with_confidence")

    partner_name = forms.CharField(label="Назва закладу", widget=forms.TextInput(attrs={
        "placeholder": "Введіть назву закладу",
        "class": "form-control",
        "id": "partner-name-field",
    }))

    partner_niche = forms.ChoiceField(label="Вид діяльності", choices=data_storage.NICHE_CHOICE,
                                      widget=forms.Select(attrs={
                                          "class": "form-control",
                                      }))

    partner_cuisine = forms.ChoiceField(label="Напрям кухні", required=False, choices=data_storage.CUISINES_CHOICE,
                                        widget=forms.Select(attrs={
                                            "class": "form-control",
                                            "placeholder": "Оберіть напрям кухні",
                                            "id": "cuisine-choice"
                                        }))

    partner_address = forms.CharField(label="Адреса", widget=forms.TextInput(attrs={
        "placeholder": "Введіть адресу закладу",
        "class": "form-control",
        "id": "partner-address-field",
    }))

    partner_postal_code = forms.CharField(label="Поштовий індекс", required=False, widget=forms.TextInput(attrs={
        "placeholder": "Введіть ваш поштовий індекс",
        "class": "form-control",
        "id": "partner-postal-code-field",
    }))

    partner_email = forms.EmailField(label="Робоча електронна адреса", widget=forms.EmailInput(attrs={
        "placeholder": "Введіть електронну адресу",
        "class": "form-control",
        "id": "partner-email-field",
    }))

    country_phone_code = forms.ModelChoiceField(
        queryset=CountryCode.objects.all(),
        label="", required=False,
        widget=CountryFlagSelect(attrs={
            "class": "form-control select-country-flag"
        }))

    partner_phone = PhoneNumberField(region="UA", label="Номер телефону", initial="+380", widget=forms.TextInput(
        attrs={"placeholder": "Номер мобільного телефону"}
    ))

    is_agree_with_confidence = forms.BooleanField(label="", widget=forms.CheckboxInput(attrs={
        "class": "check-field",
        "id": "is_agree_field",
    }))
