from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib import messages

from .forms import BusinessOwnerRegistrationForm, BusinessOwnerLoginForm, BusinessOwnerPersonalDataForm
#from .models import BusinessOwnerData
from .services import get_data_from_model


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


def owner_profile_page_third_step_view(request):
    request.session["third_page"] = True
    return render(request, "business/owner_profile_third_page.html")