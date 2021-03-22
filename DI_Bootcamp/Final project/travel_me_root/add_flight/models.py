from django.db import models
from account.models import Profile
from django.contrib.auth.models import User

# class Airport(models.Model):
#     flight_select = models.CharField(max_length=50)


# class FlightInput(models.Model):
#     user = models.ForeignKey(Profile, on_delete=models.CASCADE)
#     flight_dep = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='dep')
#     flight_arv = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arv')
#     space = models.IntegerField(max_length=30, choices=list(zip(range(1, 31), range(1, 31))))