from django import forms

from .models import BoltPartner


class AddPartnerForm(forms.ModelForm):

    class Meta:
        model = BoltPartner
        fields = ("partner_name", "partner_niche",
                  "partner_cuisine", "partner_address",
                  "partner_postal_code", "partner_email",
                  "partner_phone", "is_agree_with_confidence")


