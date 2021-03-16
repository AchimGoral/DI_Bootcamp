from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    image = models.ImageField(upload_to='../media/photos/%Y/%m/%d/')

    def __str__(self):
        if self.user:
            return self.user.username
