from django import forms


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

