from django.shortcuts import render

from .forms import DriverRegistrationForm
from .services import form_dropdown_cities_window


def driver_main_page(request):
    if request.method == "POST":
        form = DriverRegistrationForm(request.POST)
        if form.is_valid():
            pass
        else:
            pass
    else:
        form = DriverRegistrationForm()
        print(form.fields)
    countries_list = form_dropdown_cities_window()
    context = {"form": form, "countries_list": countries_list}
    return render(request, "driver/main_page.html", context)
