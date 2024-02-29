from django.urls import path

from .views import *

urlpatterns = [
    path('', driver_main_page, name="driver_main_page"),
    path('verification/<str:verification_code>/', verification_phone_number, name="number_verification"),
    path('resend-code', resend_code_view, name="resend_code"),
    path('registration/first/<str:device_ip>', registration_first_page, name="registration_first"),
    path('search/<str:device_ip>', search_car_models, name="search_cars")
]