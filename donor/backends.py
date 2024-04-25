from django.contrib.auth.backends import BaseBackend
from .models import Donor


class DonorBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = Donor.objects.get(email=email)
        except Donor.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return Donor.objects.get(pk=user_id)
        except Donor.DoesNotExist:
            return None
