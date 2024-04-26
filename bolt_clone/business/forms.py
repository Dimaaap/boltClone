from django import forms

from phonenumber_field.formfields import PhoneNumberField

from .data_storage import DataStorage
from .models import BusinessOwnerData
from .services import get_data_from_model

data_storage = DataStorage()


class BusinessOwnerRegistrationForm(forms.Form):
    owner_email = forms.EmailField(label="Робоча адреса електронної пошти", max_length=60,
                                   required=True,
                                   widget=forms.EmailInput(attrs={
                                       "class": "form-control",
                                       "id": "business-email",
                                       "placeholder": "Введіть адресу робочої електронної пошти"
                                   }))
    owner_password = forms.CharField(label="Пароль", required=True,
                                     widget=forms.PasswordInput(attrs={
                                         "class": "form-control",
                                         "id": "business-password",
                                         "placeholder": "Створити пароль"
                                     }))


    def clean_owner_email(self):
        owner_email = self.cleaned_data["owner_email"]
        if not owner_email:
            raise forms.ValidationError("Заповніть це поле")
        if get_data_from_model(BusinessOwnerData, "email", owner_email):
            raise forms.ValidationError("Підтвердіть email")
        return owner_email


    def clean_owner_password(self):
        owner_password = self.cleaned_data["owner_password"]
        if not owner_password:
            raise forms.ValidationError("Заповніть це поле")
        if len(owner_password) < 6:
            raise forms.ValidationError("Пароль надто короткий(необхідно мінімум 6 символів)")
        if all([i.isdigit() for i in owner_password]) or all([i.isalpha() for i in owner_password]):
            raise forms.ValidationError("Пароль повинен містити хоча б одну цифру і літеру")
        return owner_password


class BusinessOwnerLoginForm(forms.Form):
    owner_email = forms.EmailField(label="Адреса електронної пошти", required=True,
                                   widget=forms.EmailInput(attrs={
                                       "class": "form-control",
                                       "id": "owner_email"
                                   }))

    owner_password = forms.CharField(label="Пароль", required=False,
                                     widget=forms.PasswordInput(attrs={
                                         "class": "form-control",
                                         "id": "owner_password",
                                         "placeholder": "Введіть пароль",
                                         "name": "current_password"
                                     }))


class BusinessOwnerPersonalDataForm(forms.Form):
    owner_first_name = forms.CharField(max_length=100, label="Ім'я", required=True,
                                       widget=forms.TextInput(attrs={
                                           "class": "form-control",
                                           "id": "owner_first_name",
                                           "placeholder": "Ім'я"
                                       }))

    owner_last_name = forms.CharField(max_length=150, label="Прізвище", required=True,
                                      widget=forms.TextInput(attrs={
                                          "class": "form-control",
                                          "id": "owner_last_name",
                                          "placeholder": "Прізвище"
                                      }))
    owner_phone_number = PhoneNumberField(region="UA", label="Номер телефону",
                                          widget=forms.TextInput(attrs={
                                              "class": "form-control",
                                              "id": "owner_phone_number"
                                          }))


class BusinessCompanyDataForm(forms.Form):
    company_name = forms.CharField(max_length=200, required=True, label="Назва компанії",
                                   widget=forms.TextInput(attrs={
                                       "class": "form-control",
                                       "id": "company_name_field",
                                       "placeholder": "Наприклад: ТОВ 'Назва компанії'"
                                   }))
    company_country = forms.CharField(max_length=50, required=True, label="Країна",
                                      widget=forms.TextInput(attrs={
                                          "class": "form-control select",
                                          "id": "company_country",
                                          "readonly": "readonly"
                                      }))
    workers_count = forms.CharField(label="Штат працівників", required=True,
                                    widget=forms.TextInput(attrs={
                                        "class": "form-control select",
                                        "id": "workers_count",
                                        "placeholder": "Кількість працівників",
                                        "readonly": "readonly"
                                    }))
    promo_code = forms.CharField(label="Промокод", required=False,
                                 widget=forms.TextInput(attrs={
                                     "class": "form-control",
                                     "id": "promo_code",
                                     "placeholder": "Введіть промокод"
                                 }))


class CompanyLegalInformationForm(forms.Form):
    company_legal_name = forms.CharField(label="Юридична назва компанії", required=True,
                                         widget=forms.TextInput(attrs={
                                             "class": "form-control",
                                             "id": "company-legal-name"
                                         }))
    company_country = forms.CharField(label="Країна", required=True,
                                      widget=forms.TextInput(attrs={
                                          "class": "form-control",
                                          "id": "company-country",
                                          "readonly": "readonly"
                                      }))
    bills_email = forms.EmailField(label="Електронна скринька для рахунків", required=True,
                                   widget=forms.EmailInput(attrs={
                                       "class": "form-control",
                                       "id": "bills-email",
                                       "placeholder": "Електронна скринька для рахунків"
                                   }))
    company_address = forms.CharField(label="Юридична адреса компанії", required=True,
                                         widget=forms.TextInput(attrs={
                                             "class": "form-control",
                                             "id": "legal-company-name",
                                             "placeholder": "Юридична адреса компанії"
                                         }))
    edrpou_data = forms.CharField(max_length=8, label="ЄДРПОУ", required=True,
                                  widget=forms.TextInput(attrs={
                                      "class": "form-control",
                                      "id": "edrpou_data",
                                      "placeholder": "ЄДРПОУ"
                                  }))
    company_ipn = forms.CharField(max_length=12, label="Номер платника ПДВ", required=False,
                                  widget=forms.TextInput(attrs={
                                      "class": "form-control",
                                      "id": "company-ipn",
                                      "placeholder": "Номер платника ПДВ"
                                  }))

    def clean_edrpou_data(self):
        edrpou_data = self.cleaned_data["edrpou_data"]
        if any(not i.isdigit() for i in edrpou_data):
            raise forms.ValidationError("Неправильний формат коду ЄДРПОУ")
        return edrpou_data


    def clean_company_ipn(self):
        company_ipn = self.cleaned_data["company_ipn"]
        if any(not i.isdigit() for i in company_ipn):
            raise forms.ValidationError("Неправильний формат номеру платника ПДВ")
        return company_ipn


class ChangeUserPasswordForm(forms.Form):
    current_password = forms.CharField(max_length=200, label="Поточний пароль", required=True,
                                       widget=forms.PasswordInput(attrs={
                                           "class": "form-control",
                                           "placeholder": "Введіть поточний пароль"
                                       }))
    new_password = forms.CharField(max_length=200, required=True, label="Новий пароль",
                                   widget=forms.PasswordInput(attrs={
                                       "class": "form-control",
                                       "placeholder": "Введіть новий пароль"
                                   }))


    def clean_new_password(self):
        new_password = self.cleaned_data["new_password"]
        if len(new_password) < 6:
            raise forms.ValidationError("Довжина паролю повинна бути мінімум 6 символів")
        if all([i.isdigit() for i in new_password]) or all([i.isalpha() for i in new_password]):
            raise forms.ValidationError("Надто простий пароль. Пароль повинен містити цифри і літери")


class ChangeOwnerFullNameForm(forms.Form):
    owner_first_name = forms.CharField(max_length=100, required=True, label="Ім'я",
                                       widget=forms.TextInput(attrs={
                                           "class": "form-control",
                                           "id": "user-first-name"
                                       }))
    owner_last_name = forms.CharField(max_length=200, required=True, label="Прізвище",
                                      widget=forms.TextInput(attrs={
                                          "class": "form-control",
                                          "id": "user-last-name"
                                      }))


class ChangeOwnerEmailForm(forms.Form):
    owner_email = forms.EmailField(max_length=60, required=True, label="Електронна пошта",
                                   widget=forms.EmailInput(attrs={
                                       "class": "form-control",
                                       "id": "user-email"
                                   }))


class ChangeOwnerPhoneNumberForm(forms.Form):
    phone_number = PhoneNumberField(region="UA", label="Телефон",
                                    widget=forms.TextInput(
                                        attrs={
                                            "class": "form-control",
                                            "id": "phone-number-field"
                                        }
                                    ))


class AddPDFEmailForm(forms.Form):
    email_address = forms.EmailField(label="", required=False, widget=forms.EmailInput(
        attrs={
            "class": "form-control",
            "id": "email-address-field",
            "placeholder": "Введіть адресу електронної скриньки"
        }
    ))


class AddPromoCodeForm(forms.Form):
    promo_code = forms.CharField(label="Промокод", required=False,
                                 widget=forms.TextInput(attrs={
                                     "class": "form-control",
                                     "id": "promo-code",
                                     "placeholder": "Промокод"
                                 }))