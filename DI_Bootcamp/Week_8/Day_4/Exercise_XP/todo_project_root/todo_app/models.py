from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100, blank=False)
    details = models.TextField()
    has_been_done = models.BooleanField(null=True, default=False)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_completion = models.DateTimeField(auto_now=True, null=False)
    deadline_date = models.DateTimeField(null=False)

    def __repr__(self):
        return f"ID: {self.id} Title: {self.title}"

    def __str__(self):
        return f"ID: {self.id} Title: {self.title}"

class Category(models.Model):
    todos = models.ManyToManyField(Todo, related_name='all_todo')
    name = models.CharField(max_length=100, default='no category')
    image = models.URLField(max_length=200)

    class Meta:
        verbose_name_plural = "categories"

    def __repr__(self):
        return f"ID: {self.id} Category: {self.name}"

    def __str__(self):
        return f"ID: {self.id} Category: {self.name}"