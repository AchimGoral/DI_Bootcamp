from django.urls import path
from . import views

urlpatterns = [
    path('todo_view/', views.todo_view, name='todo_view'),
    path('display_todo/', views.display_todo, name='display_todo'),
]