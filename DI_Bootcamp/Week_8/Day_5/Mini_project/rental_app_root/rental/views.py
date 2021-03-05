from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def customer(request):
    my_customer = Customer.objects.all().order_by('last_name')
    context = {
        'my_customer': my_customer
    }
    return render(request, 'customer.html', context)

def customer_add(request):
    pass

def customer_int(request, pk):
    pass

def vehicle(request):
    my_vehicle = Vehicle_type.objects.all()
    context = {
        'my_vehicle': my_vehicle
    }
    return render(request, 'vehicle.html', context)


def vehicle_add(request):
    pass

def vehicle_int(request, pk):
    pass

def rental(request):
    my_rental = Rental.objects.all()
    context = {
        'my_rental': my_rental
    }
    return render(request, 'rental.html', context)

def rental_add(request):
    pass

def rental_int(request, pk):
    pass
