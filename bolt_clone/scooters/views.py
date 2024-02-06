from django.shortcuts import render

from .forms import ScooterSafetyReportForm, ScooterOtherReportForm
from .services import handle_first_form, handle_second_form


def scooter_main_page(request):
    return render(request, "scooters/main_page.html")


def scooter_safety_page(request):
    return render(request, 'scooters/safety_page.html')


def scooter_safety_lab_page(request):
    return render(request, 'scooters/safety_lab.html')


def scooter_report_page(request):
    second_form = ScooterOtherReportForm()
    form = ScooterSafetyReportForm()
    success = False
    if request.method == "POST":
        form_type = request.POST.get("form_type")
        if form_type == "form1":
            form = ScooterSafetyReportForm(request.POST, request.FILES)
            success = handle_first_form(form)
        elif form_type == "form2":
            second_form = ScooterOtherReportForm(request.POST)
            success = handle_second_form(second_form)
    else:
        form = ScooterSafetyReportForm()
        second_form = ScooterOtherReportForm()
        success = False
    context = {"form": form, "second_form": second_form, "success": success}
    return render(request, 'scooters/report_page.html', context)
