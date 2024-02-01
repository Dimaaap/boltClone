from django.urls import path

from .views import *


urlpatterns = [
    path('safety', scooter_safety_page, name="scooter_safety")
]