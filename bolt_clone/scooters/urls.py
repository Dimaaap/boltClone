from django.urls import path

from .views import *


urlpatterns = [
    path('', scooter_main_page, name="scooter_main_page"),
    path('safety', scooter_safety_page, name="scooter_safety"),
    path('safety-lab', scooter_safety_lab_page, name="scooter_safety_lab"),
    path('report', scooter_report_page, name='scooter_report')
]