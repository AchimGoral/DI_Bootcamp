from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    image = models.ImageField(upload_to='../media/photos/%Y/%m/%d/', default='default.jpg', blank=True, null=True)

    def drafts(self):
        return self.post_set.filter(status=0).order_by('-created')

    def __str__(self):
        return f'User: {self.user.username}'