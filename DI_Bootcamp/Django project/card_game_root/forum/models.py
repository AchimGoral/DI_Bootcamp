from django.db import models
from account.models import Profile


class Index(models.Model):
    title = models.CharField(max_length=100)
    comment = models.TextField(max_length=1000)
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    title = models.CharField(max_length=100)
    comment = models.TextField(max_length=1000)
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    index = models.ForeignKey(Index, on_delete=models.CASCADE, related_name='thread')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title