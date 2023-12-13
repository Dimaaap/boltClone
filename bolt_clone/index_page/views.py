from django.shortcuts import render
from ipware import get_client_ip

from .forms import AddPartnerForm
from .services import *


def index_page_view(request):
    return render(request, 'index_page/index_page.html')


def become_partner_view(request):
    return render(request, "index_page/become_partner_page.html")


def partner_signup_view(request):
    client_ip, is_routable = get_client_ip(request)
    if request.method == 'POST':
        form = AddPartnerForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            pass
    else:
        form = AddPartnerForm(initial={'country_phone_code': get_user_country_by_ip_service(client_ip)})
    context = {"form": form}
    return render(request, "index_page/partner_signup_page.html", context=context)
