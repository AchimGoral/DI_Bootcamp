from django.contrib import admin
from .models import Post, Comment, Category

class PostAdmin(admin.ModelAdmin):
    list_display = ('headline', 'status','created', 'profile_id', 'category')
    list_filter = ("status",)
    search_fields = ['headline', 'content']
  
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Category)