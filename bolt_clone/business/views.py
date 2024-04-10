from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

from .forms import *
from .services import *
from .models import *


data_storage = DataStorage()


def send_user_mail(subject: str, user_email: str, file_name):
    html_message = render_to_string(f"business/emails/{file_name}")
    plain_message = strip_tags(html_message)
    from_email = settings.EMAIL_HOST_USER
    to = user_email
    send_mail(subject, plain_message, from_email, [to], html_message=html_message)


def business_main_page_view(request):
    clear_session_service(request)
    return render(request, "business/main_page.html")


def business_green_page_view(request):
    return render(request, "business/green_page.html")


def business_signup_page_view(request):
    request.session["first_page"] = True
    if request.method == "POST":
        form = BusinessOwnerRegistrationForm(request.POST)
        if form.is_valid():
            owner_email, owner_password = form.cleaned_data.values()
            request.session["business_info"] = {"email": owner_email, "password": owner_password}
            return redirect(owner_profile_page_view)
    else:
        is_in_second_step = request.session.get("second_step")
        is_in_third_step = request.session.get("third_step")
        if not is_in_second_step or not is_in_third_step:
            form = BusinessOwnerRegistrationForm()
        else:
            user_email = request.session.get("business_info")["email"]
            form = BusinessOwnerRegistrationForm(initial={"owner_email": user_email})
    context = {"form": form}
    return render(request, "business/signup_page.html", context)


def business_login_page_view(request):
    if request.method == "POST":
        form = BusinessOwnerLoginForm(request.POST)
        if form.is_valid():
            user_email, user_password = form.cleaned_data.values()
            user = authenticate(request, email=user_email, password=user_password)
            if user is not None:
                login(request, user)
                return redirect(business_account_page, str(user.owner_id))
            else:
                return messages.error(request, "Неправильний логін або пароль")
    else:
        user_email = request.session.get("email", None)
        if not user_email:
            form = BusinessOwnerLoginForm()
        else:
            form = BusinessOwnerLoginForm(initial={"owner_email": user_email})
    context = {"form": form}
    return render(request, "business/login_page.html", context)


def owner_profile_page_view(request):
    if not request.session.get("first_page"):
        return redirect(business_signup_page_view)
    request.session["second_step"] = True
    if request.method == "POST":
        form = BusinessOwnerPersonalDataForm(request.POST)
        if form.is_valid():
            first_name, last_name, phone_number = form.cleaned_data.values()
            request.session["business_info"].update({"owner_first_name": first_name,
                                                     "owner_last_name": last_name,
                                                     "owner_phone_number": str(phone_number)})
            return redirect(owner_profile_page_third_step_view)
    else:
        is_in_third_page = request.session.get("third_step")
        if not is_in_third_page:
            form = BusinessOwnerPersonalDataForm(initial={"owner_phone_number": "+380"})
        else:
            owner_first_name, owner_last_name = (request.session["business_info"]["owner_first_name"],
                                                 request.session["business_info"]["owner_last_name"])
            form = BusinessOwnerPersonalDataForm(initial={"owner_phone_number": "+380",
                                                          "owner_first_name": owner_first_name,
                                                          "owner_last_name": owner_last_name
                                                          })
    context = {"form": form}
    return render(request, "business/owner_profile_page.html", context)

def owner_profile_page_third_step_view(request):
    if not request.session.get("first_page"):
        return redirect(business_signup_page_view)
    request.session["third_step"] = True
    try:
        del request.session["second_step"]
    except KeyError:
        pass
    user_phone_number = request.session["business_info"]["owner_phone_number"]
    in_drivers, in_couriers = is_in_drivers_or_couriers_service(user_phone_number)
    if request.method == "POST":
        form = BusinessCompanyDataForm(request.POST)
        if form.is_valid():
            (company_title, company_country, workers_count, *promo_code) = form.cleaned_data.values()
            country = search_country_in_model_service(company_country)
            owner_data = request.session["business_info"]
            owner_data.update({"company_name": company_title,
                               "company_employees_count": workers_count, "promo": promo_code[0]})
            user_email, user_password = owner_data["email"], owner_data["password"]
            del owner_data["email"]
            del owner_data["password"]
            try:
                new_owner = BusinessOwnerData.objects.create_user(email=user_email, password=user_password,
                                                                  **owner_data, company_country_id=country)
            except Exception as e:
                print(e)
            else:
                #login(request, new_owner, backend="business.backends.EmailAuthBackend")
                send_user_mail("Активація акаунту", new_owner.email, "business_confirmation.html")
                return redirect(business_account_page, str(new_owner.owner_id))
    else:
        form = BusinessCompanyDataForm(initial={"company_country": "🇺🇦 Україна"})
    countries_list = data_storage.COUNTRY_LIST
    employees_count = data_storage.EMPLOYEES_COUNT
    context = {"driver": in_drivers, "courier": in_couriers, "form": form, "countries_list": countries_list,
               "employees_count": employees_count}
    return render(request, "business/owner_profile_third_page.html", context)


def business_account_page(request, owner_id):
    clear_session_service(request)
    owner = get_data_from_model(BusinessOwnerData, "owner_id", owner_id)
    if not owner:
        return redirect(business_signup_page_view)
    context = {"owner_id": owner_id, "user_email": owner.email}
    return render(request, "business/account_page.html", context)