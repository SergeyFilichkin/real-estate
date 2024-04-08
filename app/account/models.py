from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from account.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(verbose_name='username', max_length=255, unique=True)
    email = models.EmailField(verbose_name='email_address')
    phone = models.CharField(verbose_name='phone_number', max_length=30, null=True, blank=True)
    date_joined = models.DateTimeField(verbose_name='date_joined', auto_now_add=True)
    is_active = models.BooleanField(verbose_name='active', default=False)
    is_staff = models.BooleanField(verbose_name='staff', default=False)

    is_verified = models.BooleanField(verbose_name='verified', default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        unique_together = ('username', 'email', 'phone')
