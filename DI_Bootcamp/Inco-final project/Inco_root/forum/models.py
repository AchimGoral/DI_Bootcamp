from django.db import models
from accounts.models import Profile

class File(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='../media/documents/')
    uploaded = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-uploaded']