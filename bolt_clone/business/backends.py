from uuid import UUID

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model



class CustomOwnerBackend(ModelBackend):
    def authenticate(self, request, owner_email=None, password=None, **kwargs):
        User = get_user_model()
        try:
            user = User.objects.get(owner_email=owner_email)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
    def get_user(self, user_id):
        User = get_user_model()
        try:
            return User.objects.get(owner_id=UUID(user_id, version=4))
        except User.DoesNotExist:
            return None

    def has_perm(self, user_obj, perm, obj=None):
        return True