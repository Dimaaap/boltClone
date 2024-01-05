from django import forms
from phonenumber_field.formfields import PhoneNumberField

from .models import City
from .db_services import get_all_fields_from_db
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

    courier_email = forms.EmailField(label="Email адреса*", required=True, widget=forms.EmailInput(
        attrs={
            "class": "form-control",
            "id": "email_field"
        }
    ))

    courier_city = forms.ModelChoiceField(label="Місто*", queryset=get_all_fields_from_db(City),
                                          widget=forms.RadioSelect(attrs={"class": "country-select"}))

    courier_is_adult = forms.ChoiceField(label="Підтвердіть, що вам виповнилось 18 років(*)",
                                         widget=forms.RadioSelect, choices=data_storage.is_adult)

    courier_is_agree_to_sms = forms.ChoiceField(label=f"Натискаюсчи 'Погоджуюсь', ви підтверджуєте, що"
                                                      f"надаєте свою згоду на отримання смс або "
                                                      f"Viber-повідомлень про наступні кроки для "
                                                      f"реєстрації кур'єром Bolt Food(*)",
                                                widget=forms.RadioSelect, choices=data_storage.is_agree_with_sms)
