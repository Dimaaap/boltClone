from django import forms
from django.core.exceptions import ObjectDoesNotExist
from phonenumber_field.formfields import PhoneNumberField

from .models import City, CourierMainInfo, FleetAddress, DeliveryMethod
from .db_services import get_all_fields_from_db, get_field_from_model
from .data_storage import DataStorage

data_storage = DataStorage()


class CourierMainInfoForm(forms.Form):

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '*')
        super(CourierMainInfoForm, self).__init__(*args, **kwargs)

    courier_first_name = forms.CharField(label="Ім'я*", required=True, widget=forms.TextInput(attrs={
        "class": "form-control",
        "id": "first_name_field"
    }))

    courier_last_name = forms.CharField(label="Прізвище*", required=True, widget=forms.TextInput(attrs={
        "class": "form-control",
        "id": "last_name_field"
    }))

    courier_phone_number = PhoneNumberField(region="UA", label="Номер телефону*")
    courier_phone_number.error_messages["invalid"] = "Некоректний формат номеру(+380501234123)"

    courier_email = forms.EmailField(label="Email адреса*", required=True, widget=forms.EmailInput(
        attrs={
            "class": "form-control",
            "id": "email_field"
        }
    ))

    courier_city = forms.ModelChoiceField(label="Місто*", queryset=get_all_fields_from_db(City),
                                          widget=forms.RadioSelect(attrs={"class": "country-select"}))

    courier_is_adult = forms.ChoiceField(label="Підтвердіть, що вам виповнилось 18 років(*)",
                                         widget=forms.RadioSelect(attrs={"id": "is-adult-field"}),
                                         choices=data_storage.is_adult)

    courier_is_agree_to_sms = forms.ChoiceField(label=f"Натискаючи 'Погоджуюсь', ви підтверджуєте, що"
                                                      f" надаєте свою згоду на отримання смс або "
                                                      f"Viber-повідомлень про наступні кроки для "
                                                      f"реєстрації кур'єром Bolt Food(*)",
                                                widget=forms.RadioSelect, choices=data_storage.is_agree_with_sms)

    courier_fleet = forms.ModelChoiceField(label="Оберіть інформаційно-консультаційний центр "
                                                 "для кур'єрів, з яким будете співпрацювати:*",
                                           queryset=get_all_fields_from_db(FleetAddress), required=False,
                                           widget=forms.RadioSelect(attrs={"class": "fleet-address-select"}))

    def clean_courier_first_name(self):
        first_name = self.cleaned_data["courier_first_name"]
        if not first_name:
            raise forms.ValidationError("Заповніть це поле, будь ласка")
        if any(i.isdigit() for i in first_name):
            raise forms.ValidationError("Ім'я не може містити цифр")
        if len(first_name) > 255:
            raise forms.ValidationError("Надто довге ім'я")
        return first_name

    def clean_courier_last_name(self):
        last_name = self.cleaned_data["courier_last_name"]
        if not last_name:
            raise forms.ValidationError("Заповніть це поле, будь ласка")
        if any(i.isdigit() for i in last_name):
            raise forms.ValidationError("Прізвище не може містити цифр")
        if len(last_name) > 255:
            raise forms.ValidationError("Надто довге прізвище")
        return last_name


class CourierDocumentsInfoForm(forms.Form):
    courier_city = forms.ModelChoiceField(label="Оберіть ваше місто*", queryset=get_all_fields_from_db(City),
                                          widget=forms.RadioSelect(attrs={"class": "country-select"}))
    credit_card_name = forms.CharField(label="Ім'я та прізвище власника картки латинськими літерами(має збігатись"
                                             "з іменем, вказаним в обліковому записі)*",
                                       required=True,
                                       max_length=150,
                                       widget=forms.TextInput(attrs={"class": "form-control", "id": "card_name_field"}))
    iban_number = forms.CharField(label="Номер банківського рахунку в міжнародному форматі (IBAN)*",
                                  required=True,
                                  max_length=40,
                                  widget=forms.TextInput(attrs={"class": "form-control",
                                                                "id": "iban_number_field"})
                                  )
    identification_number = forms.CharField(label="Ваш ідентифікаційний номер (РНОКПП)*",
                                            max_length=11, required=True,
                                            widget=forms.TextInput(attrs={"class": "form-control",
                                                                          "id": "id_number_field"}))
    bank_card_certificate = forms.FileField(label="Завантажте довідку з банку для підтвердження того, що ви"
                                                  " є власником банківського рахунку:*",
                                            required=True,
                                            widget=forms.FileInput(attrs={"class": "form-control",
                                                                          "id": "card_certificate_field"}))
    document_image = forms.ImageField(label="Завантажте фото документа, що посвідчує особу (паспорт, ID-картка "
                                            "або водійські права)*", required=True,
                                      widget=forms.FileInput(attrs={"class": "form-control",
                                                                    "id": "document_image_field"}))
    medicine_card_image = forms.ImageField(label="Завантажте фото вашої медичної книжки",
                                           required=False,
                                           widget=forms.FileInput(attrs={"class": "form-control",
                                                                         "id": "medicine_card_image"}))
    courier_image = forms.ImageField(label="Завантажте ваше фото(переконайтеся, що "
                                           "прийнамні 80% вашого обличчя добре видно)*", required=True,
                                     widget=forms.FileInput(attrs={"class": "form-control",
                                                                   "id": "courier_image_field"}))
    delivery_method = forms.ModelChoiceField(label="Оберіть ваш основний спосіб доставки*",
                                             queryset=get_all_fields_from_db(DeliveryMethod),
                                             required=True,
                                             widget=forms.CheckboxSelectMultiple
                                             )
    has_bag = forms.ChoiceField(label="Термосумка для доставок: ", required=True,
                                widget=forms.RadioSelect, choices=data_storage.has_bag)