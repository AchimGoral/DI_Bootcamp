from django.shortcuts import render, redirect
from .models import *
from .forms import *


def customer(request):
    my_customer = Customer.objects.all().order_by('last_name')
    context = {
        'my_customer': my_customer
    }
    return render(request, 'customer.html', context)


def customer_add(request):

    if request.method == "GET":
        cust_add = Customer_add()
        return render(request, 'add.html', {'cust_add':cust_add})

    if request.method == 'POST':

        cust_add = Customer_add(request.POST)

        if cust_add.is_valid():
            first_name = cust_add.cleaned_data['first_name']
            last_name = cust_add.cleaned_data['last_name']
            email = cust_add.cleaned_data['email']
            phone_number = cust_add.cleaned_data['phone_number']
            address = cust_add.cleaned_data['address']
            city = cust_add.cleaned_data['city']
            country = cust_add.cleaned_data['country']
            
            f = Customer(first_name=first_name, last_name=last_name, email=email, phone_number=phone_number, address=address, city=city, country=country)
            f.save()
            return redirect('customer')

        else:
            return render(request, 'add.html', {'cust_add':cust_add})


def customer_int(request, pk):
    one_customer = Customer.objects.get(id=pk)
    context = {
        'one_customer':one_customer
    }
    return render(request, 'customer.html', context)


def vehicle(request):
    my_vehicle = Vehicle_type.objects.all()
    context = {
        'my_vehicle': my_vehicle
    }
    return render(request, 'vehicle.html', context)


def vehicle_add(request):

    if request.method == "GET":
        veh_add = Vehicle.objects.all()
        context = {
            'veh_add':veh_add
        }
        return render(request, 'add.html', context)

    if request.method == 'POST':

        veh_add = Vehicle_add(request.POST)

        if veh_add.is_valid():
            vehicle_type = veh_add.cleaned_data['vehicle_type']
            size = veh_add.cleaned_data['size']
            real_cost = veh_add.cleaned_data['real_cost']
            
            c = Vehicle(vehicle_type=vehicle_type, size=size, real_cost=real_cost)

            t.save()
            s.save()
            c.save()
            return redirect('vehicle')
    else:
            return render(request, 'add.html', {'veh_add':veh_add})


def vehicle_int(request, pk):
    one_vehicle = Vehicle.objects.get(id=pk)
    context = {
        'one_vehicle': one_vehicle
    }
    return render(request, 'vehicle.html', context)


def rental(request):
    my_rental = Rental.objects.all().order_by('return_date')
    context = {
        'my_rental': my_rental
    }
    return render(request, 'rental.html', context)


def rental_add(request):
    pass


def rental_int(request, pk):
    one_rental = Rental.objects.get(id=pk)
    context = {
        'one_rental': one_rental
    }
    return render(request, 'rental.html', context)
