from django.shortcuts import render
from django.http import HttpResponse


def index_page_view(request):
    return render(request, 'index_page/index_page.html')


def become_partner_view(request):
    return render(request, "index_page/become_partner_page.html")


def partner_signup_view(request):
    return render(request, "index_page/partner_signup_page.html")

