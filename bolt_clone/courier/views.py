from django.shortcuts import render

from .forms import CourierMainInfoForm


def courier_main_page_view(request):
    return render(request, "courier/courier_main_page.html")


def courier_registration_view(request):
    if request.method == "POST":
        form = CourierMainInfoForm(request.POST)
        if form.is_valid():
            pass
        else:
            print(form.errors)
    else:
        form = CourierMainInfoForm()
    context = {"form": form}
    return render(request, "courier/courier_registration_page.html", context=context)