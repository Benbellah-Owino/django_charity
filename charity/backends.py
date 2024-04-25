from django.contrib.auth.backends import BaseBackend
from .models import Owner


class OwnerBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = Owner.objects.get(email=email)
        except Owner.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return Owner.objects.get(pk=user_id)
        except Owner.DoesNotExist:
            return None
