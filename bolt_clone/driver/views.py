from django.shortcuts import render


def driver_main_page(request):
    return render(request, "driver/main_page.html")
