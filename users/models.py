from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):

    username = None
    telegram_id = models.CharField(max_length=50, verbose_name='telegram_id')
    telegram_name = models.CharField(max_length=200, unique=True, verbose_name='telegram_name')

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    USERNAME_FIELD = 'telegram_name'
    REQUIRED_FIELDS = []
