from django.urls import path

from .views import *

urlpatterns = [
    path('', courier_main_page_view, name="courier_main"),
    path('registration', courier_registration_view, name="courier_registration"),
    path('registration/second_step', courier_second_step_registration_view, name="second_step"),
    path('contacts', courier_contacts_view, name="contacts"),
    path('help-center/contact-page', courier_help_center_view, name="help_center"),
    path('help-center', courier_help_center_main_page, name="help_center_main"),
    path('help-center/courier-info', courier_info_page, name="courier_info"),
    path('help-center/insurance', courier_insurance_page, name="insurance"),
    path('help-center/loyalty-program', courier_loyalty_program_page, name="loyalty_program"),
    path('help-center/referral-bonus', courier_referral_bonus_page, name="referral_bonus"),
    path('help-center/termobag', courier_termobag_page, name='termobag'),
    path('help-center/delivery_group', courier_delivery_group_page, name="delivery_group")
]
