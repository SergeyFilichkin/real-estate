from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from account.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(verbose_name='Имя', max_length=255, unique=True)
    email = models.EmailField(verbose_name='Электронная почта')
    phone = models.CharField(verbose_name='Номер телефона', max_length=30, null=True, blank=True)
    date_joined = models.DateTimeField(verbose_name='Дата и время регистрации', auto_now_add=True)
    is_active = models.BooleanField(verbose_name='Активность', default=False)
    is_staff = models.BooleanField(verbose_name='Персонал сайта', default=False)

    is_verified = models.BooleanField(verbose_name='Проверено', default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        unique_together = ('username', 'email', 'phone')
