from django.shortcuts import render


def rider_safety_page(request):
    return render(request, "rider/safety_page.html")
