from django import forms
from django.db import models
from blog.models import Post, Comment, Category
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'headline',
            'content',
            'category',
            'status',
        )
        labels = {
            'status': 'Please check to post. Empty for draft'
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            'answer',
        )