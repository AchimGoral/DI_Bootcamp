from django.db.models import Manager

class PostManager(Manager):
    def published(self):
        return self.get_queryset().filter(status=1)

    def category(self, pk):
        return self.get_queryset().filter(category__id=pk)

    def get_queryset(self):
        return super().get_queryset().order_by('-created')