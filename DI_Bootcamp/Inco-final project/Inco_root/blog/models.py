from django.db import models
from accounts.models import Profile

class Post(models.Model):
    
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    headline = models.CharField(max_length=50)
    content = models.CharField(max_length=5000)
    answers = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.headline

class Comment(models.Model):

    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    answer = models.CharField(max_length=3000)
    answer_date = models.DateTimeField(auto_now_add=True)