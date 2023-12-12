from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from ipware import get_client_ip

from .forms import AddPartnerForm
from .models import CountryCode


def get_form_select_initial_values_service():
    try:
        default_value = CountryCode.objects.get(country_official_name="Ukraine")
    except ObjectDoesNotExist:
        default_value = None
    return default_value


def index_page_view(request):
    return render(request, 'index_page/index_page.html')


def become_partner_view(request):
    return render(request, "index_page/become_partner_page.html")


def partner_signup_view(request):
    client_ip, is_routable = get_client_ip(request)
    print(client_ip)
    if request.method == 'POST':
        form = AddPartnerForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
        else:
            print(form.errors)
    else:
        form = AddPartnerForm(initial={'country_phone_code': get_form_select_initial_values_service().pk})
    context = {"form": form}
    return render(request, "index_page/partner_signup_page.html", context=context)
