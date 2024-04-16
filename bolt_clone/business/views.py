from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.core.signing import SignatureExpired, BadSignature

from .forms import *
from .services import *
from .models import *


data_storage = DataStorage()


def send_user_mail(subject: str, user_email: str, file_name: str, user_token):
    html_message = render_to_string(f"business/emails/{file_name}", {"user_token": user_token})
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
        print(is_in_second_step)
        is_in_third_step = request.session.get("third_step")
        if not is_in_second_step and not is_in_third_step:
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
        form = BusinessOwnerPersonalDataForm(initial={"owner_phone_number": "+380"})
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
                login(request, new_owner, backend="business.backends.EmailAuthBackend")
                user_token = new_owner.generate_verification_token()
                send_user_mail("Активація акаунту", new_owner.email,
                               "business_confirmation.html", user_token)
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
    owner_full_name = owner.get_user_full_name()
    context = {"owner_id": owner_id, "user_email": owner.email, "owner": owner,
               "owner_full_name": owner_full_name}
    return render(request, "business/account_page.html", context)


def verify_account_via_email_view(request, token: str):
    MAX_TOKEN_EXPIRATION_TIME = 60 * 60 * 24  #24 hours
    signer = TimestampSigner()
    try:
        user_id = signer.unsign(token, max_age=MAX_TOKEN_EXPIRATION_TIME)
        owner = get_data_from_model(BusinessOwnerData, "owner_id", user_id)
        owner.is_email_verified = True
        owner.save()
    except (SignatureExpired, BadSignature):
        return render(request, "business/failed_verification_page.html")
    else:
        return redirect(business_account_page, owner.owner_id)


def setup_company_billing_view(request, owner_id: str):
    owner = get_data_from_model(BusinessOwnerData, "owner_id", owner_id)
    if request.method == "POST":
        form = CompanyLegalInformationForm(request.POST)
        if form.is_valid():
            (company_legal_name, company_country, bills_email, company_address,
             edrpou_data, company_ipn) = form.cleaned_data.values()
            new_company_legal = CompanyLegalInformation.objects.create(company_legal_name=company_legal_name,
                                                                       bills_email=bills_email,
                                                                       company_address=company_address,
                                                                       edrpou_data=edrpou_data,
                                                                       company_ipn=company_ipn,
                                                                       owner_id=owner)
            owner.is_legal_info_verified = True
            owner.save()
            new_company_legal.save()
            return redirect(business_account_page, owner_id)

    else:
        form = CompanyLegalInformationForm(initial={"company_legal_name": owner.company_name,
                                                    "company_country": owner.company_country_id.country_title})
    context = {"form": form, "owner": owner}
    return render(request, "business/setup_company_billing_page.html", context)


def account_page_view(request, owner_id: str):
    return render(request, "business/main_account_page.html")


def setup_company_payment_view(request, owner_id: str):
    context = {"owner_id": owner_id}
    return render(request, "business/setup_company_payment_page.html", context)


def add_card_view(request, owner_id: str):
    return render(request, "business/add_card_page.html")
