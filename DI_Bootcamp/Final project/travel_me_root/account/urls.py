from django.urls import path, include
from . import views

urlpatterns = [
    path('sign_up', views.sign_up_view, name='signup'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
]