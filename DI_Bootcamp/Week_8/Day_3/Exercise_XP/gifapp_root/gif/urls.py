from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('gif_show/<int:gif_id>', views.gif_show, name='gif_show'),
    path('categories', views.categories, name='categories'),
]