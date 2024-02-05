from django import forms

COMPANIES_CHOICES = [
    ("Bolt", "Bolt"),
    ("Bird", "Bird"),
    ("Lime", "Lime"),
    ("Tier", "Tier"),
    ("Voi", "Voi"),
    ("Wind", "Wind"),
    ("Інше", "Інше")
]


class ScooterSafetyReportForm(forms.Form):
    scooter_image = forms.ImageField(label="Документація",
                                     required=True,
                                     widget=forms.FileInput(
                                         attrs={"class": "form-field-image",
                                                "id": "image-field"}))
    city = forms.CharField(max_length=200, label="Місто",
                           required=True,
                           widget=forms.TextInput(
                               attrs={"class": "form_control",
                                      "placeholder": "У якому місті знаходиться електросамокат?"}
                           ))
    address = forms.CharField(max_length=255, required=True,
                              label="Aдреса",
                              widget=forms.TextInput(
                                  attrs={"class": "form_control",
                                         "placeholder": "Де саме знаходиться електросамокат?"}
                              ))
    rent_company = forms.CharField(max_length=10,
                                   required=True,
                                   label="Компанія прокату електросамокатів",
                                   widget=forms.Select(choices=COMPANIES_CHOICES,
                                                       attrs={
                                                           "placeholder": "Оберіть компанію-провайдера"
                                                       }))
    other_rent_company = forms.CharField(max_length=20,
                                         required=False,
                                         label="Зазначте компанію-провайдера",
                                         widget=forms.TextInput(attrs={
                                             "class": "form_control",
                                             "id": "other-company_field",
                                             "placeholder": "Компанія прокату електросамокатів"
                                         }))
    scooter_id = forms.CharField(max_length=10,
                                 required=True,
                                 label="Ідентифікаційний код електросамоката",
                                 widget=forms.TextInput(attrs={
                                     "class": "form_control",
                                     "id": "scooter_id_field",
                                     "placeholder": "Введіть номер, що знаходиться біля QR-коду"
                                 }))
    problem_desc = forms.CharField(required=False,
                                   label="Опишіть проблему(необов'язково)",
                                   widget=forms.Textarea(attrs={
                                       "class": "form_textarea",
                                       "id": "problem_desc_field",
                                       "placeholder": "Коротко опишіть проблему із самокатом"
                                   }))