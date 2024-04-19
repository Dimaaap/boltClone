from django.urls import path

from .views import *

urlpatterns = [
    path('', business_main_page_view, name="business_main"),
    path("green", business_green_page_view, name="green"),
    path("signup", business_signup_page_view, name="signup"),
    path("login", business_login_page_view, name="business_login"),
    path("signup/profile", owner_profile_page_view, name="profile"),
    path("signup/profile/next", owner_profile_page_third_step_view, name="third_step"),
    path("profile/<str:owner_id>/get_started", business_account_page, name="account"),
    path("signup/verify_account/<str:token>/", verify_account_via_email_view, name="verify_account"),
    path("company/<str:owner_id>/setup/billing/legal", setup_company_billing_view, name="setup_billing"),
    path("company/<str:owner_id>/setup/billing/payment", setup_company_payment_view, name="setup_payment"),
    path("add_card/<str:owner_id>/", add_card_view, name="add_card"),
    path("company/<str:owner_id>/account", account_page_view, name="account"),
    path("company/logout", logout_user_page_view, name="logout"),
    path("company/<str:owner_id>/change_password", change_password_view, name="change_password"),
]
