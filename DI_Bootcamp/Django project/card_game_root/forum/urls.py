from django.urls import path, include
from . import views

urlpatterns=[ 
    path('thread/',views.thread,name='thread'),
    path('forum/<int:pk>',views.forum,name='forum'),
    path('single_thread/<int:pk>',views.single_thread,name='single-thread')
]