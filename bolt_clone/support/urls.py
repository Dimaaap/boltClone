from django.urls import path

from .views import *

urlpatterns = [
    path('', main_support_view, name='index_support')
]