from django.urls import path
from . import views

urlpatterns = [
    path('homepage', views.homepage, name='homepage'),
    path('homepage/<int:pk>', views.homepage_detail, name='homepage_detail'),
    path('add_film', views.add_film, name='addfilm'),
    path('add_director', views.add_director, name='adddirector'),
]