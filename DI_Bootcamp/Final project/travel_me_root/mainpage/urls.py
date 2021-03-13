from django.urls import path, include
from . import views

urlpatterns = [
    path('home', views.main_view, name='home'),
]