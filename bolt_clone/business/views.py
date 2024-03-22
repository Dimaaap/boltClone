from django.shortcuts import render


def business_main_page_view(request):
    return render(request, "business/main_page.html")