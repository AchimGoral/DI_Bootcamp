from django.db import models

# Create your models here.
class Gif(models.Model):
    title = models.CharField(max_length=50)
    url = models.URLField(max_length=200)
    uploader_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __repr__(self):
        return f"Title, ID: {self.title}, {self.id}"

    def __str__(self):
        return f"Title, ID: {self.title}, {self.id}"


class Category(models.Model):
    name = models.CharField(max_length=50)
    gifs = models.ManyToManyField(Gif, related_name='all_gifs', blank=True)

    def __repr__(self):
        return f"Name, ID: {self.name}, {self.id}"

    def __str__(self):
        return f"Name, ID: {self.name}, {self.id}"