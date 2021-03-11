from django.urls import path, include
from . import views

urlpatterns = [
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('profile/<int:pk>', views.profile, name='profile'),
    path('edit_user', views.profile_edit, name='profile_edit'),
    path('sign_up', views.sign_up, name='sign_up'),
]