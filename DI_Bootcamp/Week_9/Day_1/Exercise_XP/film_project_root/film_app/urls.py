from django.urls import path
from . import views

urlpatterns = [
    path('homepage', views.homepage, name='homepage'),
    path('add_film', views.addFilm, name='addFilm'),
    path('add_director', views.AddDirector.as_view(), name='AddDirector'),
]