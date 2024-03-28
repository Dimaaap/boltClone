from django.urls import path

from .views import *

urlpatterns = [
    path('', business_main_page_view, name="business_main"),
    path("green", business_green_page_view, name="green"),
    path("signup", business_signup_page_view, name="signup")
]
