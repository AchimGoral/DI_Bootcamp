from django.db import models
from accounts.models import Profile
from .managers import PostManager


class Post(models.Model):
    
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    # topic = models.IntegerField(default=5)
    headline = models.CharField(max_length=50)
    content = models.TextField()
    likes = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    objects = PostManager()

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.headline

class Comment(models.Model):

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    answer = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
            ordering = ['-created']

    def __str__(self):
        return f"{self.profile} | Post ID: {self.post.id}"