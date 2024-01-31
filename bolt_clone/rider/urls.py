from django.urls import path

from .views import *


urlpatterns = [
    path('safety', rider_safety_page, name="rider_safety")
]