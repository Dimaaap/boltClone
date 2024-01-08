from django.urls import path

from .views import *

urlpatterns = [
    path('', courier_main_page_view, name="courier_main"),
    path('registration', courier_registration_view, name="courier_registration"),
    path('registration/second_step>', courier_second_step_registration_view, name="second_step")
]
