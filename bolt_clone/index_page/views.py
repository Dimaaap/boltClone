from django.shortcuts import render, redirect
import logging

from .db_services import get_all_objects_from_db
from .forms import AddPartnerForm
from .models import CuisineCategory

logger = logging.getLogger("main")


def index_page_view(request):
    return render(request, 'index_page/index_page.html')


def become_partner_view(request):
    return render(request, "index_page/become_partner_page.html")


def partner_signup_view(request):
    logger.info("User on the page")
    all_cuisine_categories = list(get_all_objects_from_db(CuisineCategory))
    if request.method == 'POST':
        form = AddPartnerForm(request.POST)
        logger.info(f"User {request.user} send a data in partner signup form ")
        if form.is_valid():
            form.save()
            return redirect(account_information_view)
        else:
            logger.warning(f"User signup form returns an error - {form.errors}")
    else:
        form = AddPartnerForm()
    context = {"form": form, "cuisines": all_cuisine_categories}
    return render(request, "index_page/partner_signup_page.html", context=context)


def account_information_view(request):
    return render(request, "index_page/account_information_page.html")