from django.shortcuts import render


def main_support_view(request):
    return render(request, "support/main_support_page.html")
