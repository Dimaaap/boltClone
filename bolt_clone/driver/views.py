from django.shortcuts import render

from .forms import DriverRegistrationForm


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
    context = {"form": form}
    return render(request, "driver/main_page.html", context)
