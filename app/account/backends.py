from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

User = get_user_model()


class AuthBackend(ModelBackend):
    def user_can_authenticate(self, user):
        return True

    def authenticate(self, request, username=None, password=None, **kwargs):
        user = User.objects.get(Q(username=username) | Q(email=username) | Q(phone=username))
        return user if user.check_password(password) else None
