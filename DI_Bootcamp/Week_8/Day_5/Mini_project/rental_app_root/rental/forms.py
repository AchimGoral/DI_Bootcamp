from django import forms
from .models import *

class Customer_add(forms.Form):
    first_name = forms.CharField(max_length=30, required=True, widget = forms.TextInput(
        attrs={
            'placeholder': 'First name'
        })
    )
    last_name = forms.CharField(max_length=30, required=True, widget = forms.TextInput(
        attrs={
            'placeholder': 'Last name'
        })
    )
    email = forms.EmailField(max_length=100, required=True, widget = forms.EmailInput(
        attrs={
            'placeholder': 'Email'
        })
    )
    phone_number = forms.CharField(max_length=20, required=False, widget = forms.TextInput(
        attrs={
            'placeholder': 'Phone-number'
        })
    )
    address = forms.CharField(max_length=100, required=False, widget = forms.TextInput(
        attrs={
            'placeholder': 'Address'
        })
    )
    city = forms.CharField(max_length=100, required=False, widget = forms.TextInput(
        attrs={
            'placeholder': 'City'
        })
    )
    country = forms.CharField(max_length=100, required=False, widget = forms.TextInput(
        attrs={
            'placeholder': 'Country'
        })
    )


class Rental_add(forms.Form):
    customer = forms.IntegerField(required=True)
    vehicle = forms.IntegerField(required=True)


class Vehicle_add(forms.Form):
    vehicle_type = forms.CharField()
    size = forms.CharField()
    real_cost = forms.FloatField(required=False, widget=forms.NumberInput())