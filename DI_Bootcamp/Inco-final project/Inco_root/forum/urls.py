from django.urls import path, include
from . import views

urlpatterns = [
    path('forum/', views.forum_view, name='forum'),
    path('forum/forum_entry/', views.forum_entry_view, name='forum-entry'),
    path('forum/forum_file/<int:pk>', views.forum_file_view, name='forum-file'),
]