from django.shortcuts import render


def scooter_safety_page(request):
    return render(request, 'scooters/safety_page.html')