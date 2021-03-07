from django import forms
from .models import *

class Customer_add(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class Rental_add(forms.Form):
    customer = forms.IntegerField(required=True)
    vehicle = forms.IntegerField(required=True)


class Vehicle_add(forms.Form):
    vehicle_type = forms.CharField()
    size = forms.CharField()
    real_cost = forms.FloatField(required=False, widget=forms.NumberInput())