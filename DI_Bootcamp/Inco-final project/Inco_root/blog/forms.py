from django import forms
from blog.models import Post, Comment
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'headline',
            'content'
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'answer'
        ]