from django.db import models

# Create your models here.
class Vehicle_type(models.Model):
    name = models.CharField(max_length=100)

    def __repr__(self):
        return f"{self.name}"

    def __str__(self):
        return f"{self.name}"


class Vehicle_size(models.Model):
    name = models.CharField(max_length=100)

    def __repr__(self):
        return f"{self.name}"

    def __str__(self):
        return f"{self.name}"


class Customer(models.Model):
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    email = models.EmailField(blank=False, max_length=254, unique=True)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Vehicle(models.Model):
    vehicle_type = models.ForeignKey(Vehicle_type, on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    real_cost = models.FloatField(default=0)
    size = models.ForeignKey(Vehicle_size, on_delete=models.SET_NULL, null=True)

    def __repr__(self):
        return f"{self.vehicle_type} | {self.size}"

    def __str__(self):
        return f"{self.vehicle_type} | {self.size}"


class Rental(models.Model):
    rental_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True)

    def __repr__(self):
        return f"{self.customer} {self.vehicle}"

    def __str__(self):
        return f"{self.customer} {self.vehicle}"

class Rental_rate(models.Model):
    daily_rate = models.FloatField(default=0)
    vehicle_type = models.ForeignKey(Vehicle_type, on_delete=models.SET_NULL, null=True)
    vehicle_size = models.ForeignKey(Vehicle_size, on_delete=models.SET_NULL, null=True)
    
    def __repr__(self):
        return f"{self.vehicle_type} | {self.vehicle_size} | Daily rate: {self.daily_rate}"

    def __str__(self):
        return f"{self.vehicle_type} | {self.vehicle_size} | Daily rate: {self.daily_rate}"