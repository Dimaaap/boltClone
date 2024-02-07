from django.urls import path

from .views import *

urlpatterns = [
    path('', driver_main_page, name="driver_main_page"),
]