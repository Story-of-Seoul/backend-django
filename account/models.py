from pickle import TRUE
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin, User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    nickname = models.CharField(max_length=20)
    age = models.IntegerField()
    region = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    def __str__(self):
        return self.nickname

