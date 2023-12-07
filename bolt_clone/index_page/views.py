from django.shortcuts import render

from .forms import AddPartnerForm
from .models import CountryCode


def index_page_view(request):
    return render(request, 'index_page/index_page.html')


def become_partner_view(request):
    return render(request, "index_page/become_partner_page.html")


def partner_signup_view(request):
    ukraine_code = CountryCode.objects.get(country_official_name="Ukraine")
    form = AddPartnerForm(initial={"country_phone_code": ukraine_code.pk})
    if request.method == 'POST':
        form = AddPartnerForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
        else:
            print(form.errors)
    context = {"form": form}
    return render(request, "index_page/partner_signup_page.html", context=context)

