from django import forms
from .models import File
from django.contrib.auth.models import User


class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('description', 'document', )
