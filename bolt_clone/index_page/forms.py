from django import forms
from phonenumber_field.formfields import PhoneNumberField

from .models import BoltPartner
from .data_storage import DataStorage

data_storage = DataStorage()


class AddPartnerForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("label_suffix", "")
        super(AddPartnerForm, self).__init__(*args, **kwargs)

    class Meta:
        model = BoltPartner
        fields = ("partner_name", "partner_niche",
                  "partner_cuisine", "partner_address",
                  "partner_postal_code", "partner_email",
                  "partner_phone", "is_agree_with_confidence")

    partner_name = forms.CharField(label="Назва закладу", widget=forms.TextInput(attrs={
        "placeholder": "Введіть назву закладу",
        "class": "form-control",
        "id": "partner-name-field"
    }))

    partner_niche = forms.ChoiceField(label="Вид діяльності", choices=data_storage.NICHE_CHOICE,
                                      widget=forms.Select(attrs={
                                          "class": "form-control"
                                      }))

    partner_address = forms.CharField(label="Адреса", widget=forms.TextInput(attrs={
        "placeholder": "Введіть адресу закладу",
        "class": "form-control",
        "id": "partner-address-field"
    }))

    partner_postal_code = forms.CharField(label="Поштовий індекс", widget=forms.TextInput(attrs={
        "placeholder": "Введіть ваш поштовий індекс",
        "class": "form-control",
        "id": "partner-postal-code-field"
    }))

    partner_email = forms.EmailField(label="Робоча електронна адреса", widget=forms.EmailInput(attrs={
        "placeholder": "Введіть електронну адресу",
        "class": "form-control",
        "id": "partner-email-field"
    }))

    partner_phone = PhoneNumberField(region="UA", label="Номер телефону", initial="+380", widget=forms.TextInput(
        attrs={"placeholder": "Номер мобільного телефону"}
    ))

    is_agree_with_confidence = forms.BooleanField(label="", widget=forms.CheckboxInput(attrs={
        "class": "check-field",
        "id": "is_agree_field"
    }))
