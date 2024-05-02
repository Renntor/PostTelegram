from django.db import models
from django.conf import settings
from users.models import NULLABLE


class Post(models.Model):
    """
    Model Post
    """
    post_id = models.PositiveIntegerField(verbose_name='post id', **NULLABLE)
    post = models.CharField(max_length=500, verbose_name='post')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='owner')

    def __str__(self):
        return self.post

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'

