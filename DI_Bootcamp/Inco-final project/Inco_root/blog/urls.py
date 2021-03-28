from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_view, name='blog'),
    path('new_entry', views.new_entry_view, name='new-entry'),
    path('blog_drafts', views.blog_draft_view, name='blog-drafts'),
    path('delete/<int:pk>', views.blog_delete_view, name='blog-delete'),
    path('edit/<int:pk>', views.blog_edit_view, name='blog-edit'),
    path('blog_entry/<int:pk>', views.blog_entry_view, name='blog-entry'),
    path('blog_like/<int:pk>', views.blog_like_view, name='blog-like'),
]