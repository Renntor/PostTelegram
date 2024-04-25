from django.db import models
from django.conf import settings


class Post(models.Model):
    """
    Model Post
    """
    post_id = models.PositiveIntegerField(verbose_name='post id')
    post = models.CharField(max_length=500, verbose_name='post')
    count_like = models.IntegerField(verbose_name='count like', default=0)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='owner')

    def __str__(self):
        return self.post

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'


class Commentary(models.Model):

    comment = models.CharField(max_length=200, verbose_name='commentary')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name = 'commentary'
        verbose_name_plural = 'comments'
