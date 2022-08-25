from django.db import models

# Create your models here.


class NewsPolicy(models.Model):
    title = models.TextField()
    url = models.TextField()
    content = models.TextField()
    type = models.CharField(max_length=20)
    category = models.CharField(max_length=10)