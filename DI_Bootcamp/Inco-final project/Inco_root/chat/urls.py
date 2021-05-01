from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.room_base_view, name='room_base'),
    path('<str:room_name>/', views.room_view, name='room_chat'),
]