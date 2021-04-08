from django.db import models
from accounts.models import Profile
from .managers import PostManager


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    

class Post(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="post_category")
    likes = models.ManyToManyField(Profile, default=0, related_name="blog_like")
    headline = models.CharField(max_length=100)
    content = models.TextField()
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

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="comment_profile")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comment_post")
    answer = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return f"{self.profile} | Post ID: str{self.post.id}"