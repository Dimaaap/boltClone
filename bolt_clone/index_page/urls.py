from django.urls import path, include

from .views import *

urlpatterns = [
    path('', index_page_view, name="index_page")
]