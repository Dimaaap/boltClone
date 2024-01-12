import logging

from django.shortcuts import render, redirect

from .forms import CourierMainInfoForm, CourierDocumentsInfoForm
from .services import save_main_courier_form

logger = logging.getLogger("main")


def courier_main_page_view(request):
    return render(request, "courier/courier_main_page.html")


def courier_registration_view(request):
    if request.method == "POST":
        form = CourierMainInfoForm(request.POST)
        if form.is_valid():
            save_main_courier_form(request, form)
            logger.info(f"New courier with email {form.cleaned_data['courier_email']} signed up")
            return redirect(courier_second_step_registration_view)
        else:
            logger.warning(f"form return error {form.errors}")
    else:
        form = CourierMainInfoForm()
    context = {"form": form}
    return render(request, "courier/courier_registration_page.html", context=context)


def courier_second_step_registration_view(request):
    if request.method == "POST":
        form = CourierDocumentsInfoForm(request.POST)
        if form.is_valid():
            pass
        else:
            pass
    else:
        form = CourierDocumentsInfoForm()
    context = {"form": form}
    return render(request, "courier/second_step_page.html", context=context)


def courier_contacts_view(request):
    return render(request, "courier/contact_page.html")


def courier_help_center_view(request):
    return render(request, "courier/help_center.html")


def courier_help_center_main_page(request):
    return render(request, "courier/help_center_main.html")


def courier_info_page(request):
    return render(request, "courier/info_page.html")


def courier_insurance_page(request):
    return render(request, "courier/insurance_page.html")
