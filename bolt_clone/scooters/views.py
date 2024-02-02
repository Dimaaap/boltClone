from django.shortcuts import render


def scooter_safety_page(request):
    return render(request, 'scooters/safety_page.html')


def scooter_safety_lab_page(request):
    return render(request, 'scooters/safety_lab.html')


def scooter_report_page(request):
    return render(request, 'scooters/report_page.html')
