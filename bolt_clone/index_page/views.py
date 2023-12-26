from django.shortcuts import render

from .db_services import get_all_objects_from_db
from .forms import AddPartnerForm
from .models import CuisineCategory


def index_page_view(request):
    return render(request, 'index_page/index_page.html')


def become_partner_view(request):
    return render(request, "index_page/become_partner_page.html")


def partner_signup_view(request):
    all_cuisine_categories = list(get_all_objects_from_db(CuisineCategory))
    if request.method == 'POST':
        form = AddPartnerForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
        else:
            pass
    else:
        form = AddPartnerForm()
    context = {"form": form, "cuisines": all_cuisine_categories}
    return render(request, "index_page/partner_signup_page.html", context=context)
