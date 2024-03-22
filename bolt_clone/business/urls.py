from django.urls import path

from .views import *

urlpatterns = [
    path('', business_main_page_view, name="business_main"),
]
