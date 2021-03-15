from django.urls import path, include
from . import views

urlpatterns = [
    path('index', views.index_view, name='index'),
    path('index/<int:pk>', views.index_view_pk, name='index_pk'),
    path('thread/<int:pk>', views.thread_view, name='thread'),
]