from django.urls import path

from .views import *

urlpatterns = [
    path('', driver_main_page, name="driver_main_page"),
    path('verification/<str:verification_code>/', verification_phone_number, name="number_verification")
]