from django.db import models
from accounts.models import Profile
from .managers import PostManager


class Post(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    headline = models.CharField(max_length=50)
    content = models.TextField()
    likes = models.ManyToManyField(Profile, related_name="blog_like", default=None, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    objects = PostManager()

    class Meta:
        ordering = ['-updated']

    def sum_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.headline

class Comment(models.Model):

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    answer = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return f"{self.profile} | Post ID: str{self.post.id}"