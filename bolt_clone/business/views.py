import re

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.core.signing import SignatureExpired, BadSignature
from django.contrib.auth.decorators import login_required
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.conf import settings

from .forms import *
from .services import *
from .models import *

data_storage = DataStorage()


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
        if not is_in_second_step and not is_in_third_step:
            form = BusinessOwnerRegistrationForm()
        else:
            user_email = request.session.get("business_info")["email"]
            form = BusinessOwnerRegistrationForm(initial={"owner_email": user_email})
    context = {"form": form}
    return render(request, "business/signup_page.html", context)


def business_login_page_view(request):
    if request.method == "POST":
        print("Here")
        form = BusinessOwnerLoginForm(request.POST)
        if form.is_valid():
            print("form is valid")
            user_email, user_password = form.cleaned_data.values()
            user = authenticate(request, email=user_email, password=user_password)
            if user is not None:
                login(request, user)
                return redirect(business_account_page, str(user.owner_id))
            else:
                return messages.error(request, "Неправильний логін або пароль")
        else:
            return messages.error(request, "Помилка")
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


@login_required(login_url="business_login")
def business_account_page(request, owner_id):
    clear_session_service(request)
    owner = get_data_from_model(BusinessOwnerData, "owner_id", owner_id)
    if not owner:
        return redirect(business_signup_page_view)
    owner_full_name = owner.get_user_full_name()
    context = {"owner_id": owner_id, "user_email": owner.email, "owner": owner,
               "owner_full_name": owner_full_name}
    return render(request, "business/account_page.html", context)


@login_required(login_url="business_login")
def verify_account_via_email_view(request, token: str):
    MAX_TOKEN_EXPIRATION_TIME = 60 * 60 * 24  # 24 hours
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


@login_required(login_url="business_login")
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


@login_required(login_url="business_login")
def account_page_view(request, owner_id: str):
    owner = get_data_from_model(BusinessOwnerData, "owner_id", owner_id)
    if request.method == "POST":
        form = ChangeUserPasswordForm(request.POST)
        change_email_form = None
        change_full_name_form = None
        change_phone_number_form = None
        if form.is_valid():
            old_password, new_password = form.cleaned_data.values()
            if not compare_owner_passwords(old_password, owner_id):
                return messages.error(request, "Неправильно введений старий пароль")
            else:
                owner.set_password(new_password)
                try:
                    owner.save()
                except Exception as e:
                    print(e)
                else:
                    return redirect(business_account_page, owner_id)
    else:
        form = ChangeUserPasswordForm()
        change_full_name_form = ChangeOwnerFullNameForm(initial={"owner_first_name": owner.owner_first_name,
                                                                 "owner_last_name": owner.owner_last_name})
        change_email_form = ChangeOwnerEmailForm(initial={"owner_email": owner.email})
        change_phone_number_form = ChangeOwnerPhoneNumberForm(initial={"phone_number": owner.owner_phone_number})
    owner = get_data_from_model(BusinessOwnerData, "owner_id", owner_id)
    owner_full_name = owner.get_user_full_name()
    context = {"owner_id": owner_id, "owner": owner, "full_name": owner_full_name, "form": form,
               "change_full_name_form": change_full_name_form, "change_email_form": change_email_form,
               "change_phone_number_form": change_phone_number_form}
    return render(request, "business/main_account_page.html", context)


def setup_company_payment_view(request, owner_id: str):
    context = {"owner_id": owner_id}
    return render(request, "business/setup_company_payment_page.html", context)


def logout_user_page_view(request):
    logout(request)
    return redirect(business_login_page_view)


@csrf_exempt
@require_POST
def change_password_view(request, owner_id):
    owner = get_data_from_model(BusinessOwnerData, "owner_id", owner_id)
    if request.method == "POST":
        current_password, new_password = request.POST.get("current_password"), request.POST.get("new_password")
        if not check_password(current_password, owner.password):
            return JsonResponse({"form_error": "Неправильно введений старий пароль", "field": 1})
        if not validate_password_service(new_password):
            return JsonResponse({"form_error": "Надто простий пароль. Він повинен містити хоча б одну цифру і літеру",
                                 "field": 2})
        owner.set_password(new_password)
        owner.save()
        return JsonResponse({"success": True, "owner_id": owner_id})
    else:
        return JsonResponse({"error": "asdsadas"})


def add_card_view(request, owner_id: str):
    return render(request, "business/add_card_page.html")


@csrf_exempt
@require_POST
def change_user_name_view(request, owner_id: str):
    owner = get_data_from_model(BusinessOwnerData, "owner_id", owner_id)
    if request.method == "POST":
        first_name, last_name = request.POST.get("owner_first_name"), request.POST.get("owner_last_name")
        if first_name and last_name:
            if not check_input_username_service(first_name, last_name):
                return JsonResponse({"form_error": "Некоректне ім'я або прізвище"})
            else:
                owner.owner_first_name = first_name
                owner.owner_last_name = last_name
                owner.save()
            return JsonResponse({"success": True, "owner_id": owner_id})
        else:
            return JsonResponse({"form_error": "Заповніть всі поля форми", "field": 1})
    else:
        return JsonResponse({"error": "WTF?"})


@csrf_exempt
@require_POST
def change_email_view(request, owner_id: str):
    owner = get_data_from_model(BusinessOwnerData, "owner_id", owner_id)
    if request.method == "POST":
        email = request.POST.get("owner_email")
        if email:
            if not check_user_email_service(email):
                return JsonResponse({"form_error": "Некоректна email-адреса"})
            else:
                owner.email = email
                owner.is_email_verified = False
                owner.save()
                owner_token = owner.generate_verification_token()
                send_user_mail("Підтвердження email", owner.email,
                               "email_confirmation.html", owner_token)
                owner.is_email_verified = True
                owner.save()
            return JsonResponse({"success": True, "owner_id": owner_id})
        else:
            return JsonResponse({"form_error": "Заповніть поле форми", "field": 1})
    else:
        return JsonResponse({"error": "WTF?"})


@csrf_exempt
@require_POST
def change_phone_number_view(request, owner_id: str):
    owner = get_data_from_model(BusinessOwnerData, "owner_id", owner_id)
    if request.method == "POST":
        phone_number = request.POST.get("phone_number")
        if phone_number:
            if not check_user_phone_number_service(phone_number):
                return JsonResponse({"form_error": "Неправильний формат номеру"})
            else:
                owner.owner_phone_number = phone_number
                owner.save()
                return JsonResponse({"success": True, "owner_id": owner_id})
        else:
            return JsonResponse({"form_error": "Заповніть поле форми"})
    else:
        return JsonResponse({"error": "WTF?"})


def check_user_email_service(user_email: str):
    try:
        validate_email(user_email)
    except ValidationError as e:
        return False
    return True


def check_user_phone_number_service(phone_number: str):
    return re.match(settings.NUMBER_PATTERN, phone_number)
