from django.urls import path
from . import views

urlpatterns = [
    path('customer/', views.customer, name='customer'),
    path('customer/add/', views.customer_add, name='customer_add'),
    path('customer/<int:pk>', views.customer_int, name='customer_int'),
    path('vehicle/', views.vehicle, name='vehicle'),
    path('vehicle/add/', views.vehicle_add, name='vehicle_add'),
    path('vehicle/<int:pk>', views.vehicle_int, name='vehicle_int'),
    path('rental/', views.rental, name='rental'),
    path('rental/add/', views.rental_add, name='rental_add'),
    path('rental/<int:pk>', views.rental_int, name='rental_int'),
]