from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib import messages

from .forms import BusinessOwnerRegistrationForm
from .models import BusinessOwnerData


def business_main_page_view(request):
    return render(request, "business/main_page.html")


def business_green_page_view(request):
    return render(request, "business/green_page.html")


def business_signup_page_view(request):
    if request.method == "POST":
        form = BusinessOwnerRegistrationForm(request.POST)
        if form.is_valid():
            owner_email, owner_password = form.cleaned_data.values()
            hashed_password = make_password(owner_password)
            new_owner = BusinessOwnerData.objects.create(owner_email=owner_email, owner_password=hashed_password)
            try:
                new_owner.save()
                return redirect(owner_profile_page_view)
            except Exception as e:
                print(e)
                return messages.error(request, "Сталась помилка ресєтрації")

    else:
        form = BusinessOwnerRegistrationForm()
    context = {"form": form}
    return render(request, "business/signup_page.html", context)


def owner_profile_page_view(request):
    return render(request, "business/owner_profile_page.html")