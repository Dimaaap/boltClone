from django.urls import path

from .views import *

urlpatterns = [
    path('', driver_main_page, name="driver_main_page"),
    path('verification/<str:verification_code>/', verification_phone_number, name="number_verification"),
    path('resend-code', resend_code_view, name="resend_code"),
    path('registration/first/<str:device_ip>', registration_first_page, name="registration_first"),
    path('registration/second/<str:device_ip>', registration_second_page, name="registration_second"),
    path('registration/third/<str:device_ip>', registration_third_page, name="registration_third"),
    path('registration/finished', finish_registration_page, name="finish_registration"),
    path('search/<str:device_ip>', search_car_models, name="search_cars"),
    path('search_car_model/<str:device_ip>/<str:brand>/', search_car_models_by_car,
         name="get_car_models"),
    path('save_file/<str:field_name>/<str:exp_time>/', save_file_view, name="save_file"),
    path('delete_file/<str:field_name>/', delete_file_view, name="delete_file"),
]