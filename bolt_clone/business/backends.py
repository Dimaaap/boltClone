from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

user_model = get_user_model()


class EmailAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None or password is None:
            return
        try:
            user = user_model.objects.get(email=username)
            if user.check_password(password):
                return user
        except user_model.DoesNotExist:
            raise ValidationError("Invalid login credentials")

    def get_user(self, user_id):
        try:
            return user_model.objects.get(pk=user_id)
        except user_model.DoesNotExist:
            return None
