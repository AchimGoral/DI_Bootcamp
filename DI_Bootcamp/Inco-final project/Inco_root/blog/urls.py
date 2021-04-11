from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_view, name='home'),
    path('blog/', views.blog_view, name='blog'),
    path('blog/new_entry/', views.new_entry_view, name='new-entry'),
    path('blog/blog_drafts/', views.blog_draft_view, name='blog-drafts'),
    path('blog/delete/<int:pk>', views.blog_delete_view, name='blog-delete'),
    path('blog/edit/<int:pk>', views.blog_edit_view, name='blog-edit'),
    path('blog/blog_entry/<int:pk>', views.blog_entry_view, name='blog-entry'),
    path('blog_like/', views.blog_like_view, name='blog-like'),
    path('blog/category/<int:pk>', views.category_view, name='category-view'),
]