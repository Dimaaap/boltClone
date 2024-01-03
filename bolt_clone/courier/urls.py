from django.urls import path

from .views import *

urlpatterns = [
    path('', courier_main_page_view, name="courier_main")
]
