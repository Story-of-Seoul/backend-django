from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
from account.models import Profile


class Board(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='boards')
    profile = models.ForeignKey(Profile,  on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    contents = models.TextField()
    request_data_type = models.CharField(max_length=64, blank=True)
    answer = models.TextField(blank=True)
    processing_status = models.CharField(max_length=12, blank=True)
    board_type = models.CharField(max_length=12)
    likes = models.ManyToManyField(User, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()


