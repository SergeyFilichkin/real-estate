from django.db.models import Q

from account.models import User


class AuthBackend(object):
    supports_object_permissions = True
    supports_anonymous_user = False
    supports_inactive_user = False

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

    def authenticate(self, request, username, password):
        try:
            user = User.objects.get(
                Q(username=username) | Q(email=username) | Q(phone=username)
            )
        except User.DoesNotExist:
            return None

        return user if user.check_password(password) else None
