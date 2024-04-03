from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password

from .forms import *
from .data_storage import DataStorage
from .services import get_data_from_model, filter_data_from_model
from driver.models import Driver
from courier.models import CourierMainInfo
from .models import *


data_storage = DataStorage()


def business_main_page_view(request):
    clear_session_service(request)
    return render(request, "business/main_page.html")


def business_green_page_view(request):
    return render(request, "business/green_page.html")


def clear_session_service(request):
    session_keys = [i for i in request.session.keys() if not i.startswith("_")
                    and i != 'google-oauth2_state' and i != 'device_ip' and i != 'social_auth_last_login_backend']
    for i in session_keys:
        del request.session[i]

def business_signup_page_view(request):
    if request.method == "POST":
        form = BusinessOwnerRegistrationForm(request.POST)
        if form.is_valid():
            owner_email, owner_password = form.cleaned_data.values()
            hashed_password = make_password(owner_password)
            request.session["business_info"] = {"business_email": owner_email, "business_password": hashed_password}
            return redirect(owner_profile_page_view)
    else:
        is_in_second_step = request.session.get("second_step")
        if not is_in_second_step:
            form = BusinessOwnerRegistrationForm()
        else:
            user_email = request.session.get("business_info")["business_email"]
            form = BusinessOwnerRegistrationForm(initial={"owner_email": user_email})
    context = {"form": form}
    return render(request, "business/signup_page.html", context)


def business_login_page_view(request):
    if request.method == "POST":
        form = BusinessOwnerLoginForm(request.POST)
        if form.is_valid():
            pass
    else:
        user_email = request.session.get("owner_email", None)
        if not user_email:
            form = BusinessOwnerLoginForm()
        else:
            form = BusinessOwnerLoginForm(initial={"owner_email": user_email})
    context = {"form": form}
    return render(request, "business/login_page.html", context)


def owner_profile_page_view(request):
    request.session["second_step"] = True
    print(request.session["business_info"])
    if request.method == "POST":
        form = BusinessOwnerPersonalDataForm(request.POST)
        if form.is_valid():
            first_name, last_name, phone_number = form.cleaned_data.values()
            request.session["business_info"].update({"first_name": first_name,
                                                         "last_name": last_name,
                                                         "phone_number": str(phone_number)})
            return redirect(owner_profile_page_third_step_view)
    else:
        form = BusinessOwnerPersonalDataForm(initial={"owner_phone_number": "+380"})
    context = {"form": form}
    return render(request, "business/owner_profile_page.html", context)


def is_in_drivers_or_couriers_service(phone_number: str):
    driver = get_data_from_model(Driver, "driver_phone_number", phone_number)
    courier = filter_data_from_model(CourierMainInfo, "courier_phone_number", phone_number)
    return [driver, courier]

def owner_profile_page_third_step_view(request):
    request.session["third_page"] = True
    user_phone_number = request.session["business_info"]["phone_number"]
    in_drivers, in_couriers = is_in_drivers_or_couriers_service(user_phone_number)
    if request.method == "POST":
        form = BusinessCompanyDataForm(request.POST)
        if form.is_valid():
            (company_title, company_country, workers_count, *promo_code) = form.cleaned_data.values()
            country = search_country_in_model_service(company_country)
            owner_data = request.session["business_info"]
            owner_data.update({"company_name": company_title, "company_country_id": company_country,
                               "company_employees_count": workers_count, "promo": promo_code[0]})
            (owner_email, owner_password, owner_first_name, owner_last_name, owner_phone_number,
             company_name, company_country_id, company_employees_count, promo) = owner_data.values()
            company_country_id = country
            try:
                new_owner = BusinessOwnerData.objects.create(
                    owner_email=owner_email,
                    owner_password=owner_password,
                    owner_first_name=owner_first_name,
                    owner_last_name=owner_last_name,
                    owner_phone_number=owner_phone_number,
                    company_name=company_name,
                    company_country_id=company_country_id,
                    company_employees_count=company_employees_count,
                    promo=promo
                )
                new_owner.save()
            except Exception as e:
                print(e)
    else:
        form = BusinessCompanyDataForm(initial={"company_country": "🇺🇦 Україна"})
    countries_list = data_storage.COUNTRY_LIST
    employees_count = data_storage.EMPLOYEES_COUNT
    context = {"driver": in_drivers, "courier": in_couriers, "form": form, "countries_list": countries_list,
               "employees_count": employees_count}
    return render(request, "business/owner_profile_third_page.html", context)


def search_country_in_model_service(company_country: str):
    company_country = company_country[2:].lstrip()
    country = get_data_from_model(BusinessCountries, "country_title", company_country)
    return country