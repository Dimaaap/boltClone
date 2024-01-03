from django.shortcuts import render


def courier_main_page_view(request):
    return render(request, "courier/courier_main_page.html")
