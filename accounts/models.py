from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db import models
from django.conf import settings

class Airport(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)  # e.g. JFK, LHR
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.code} - {self.city}"


class Aircraft(models.Model):
    name = models.CharField(max_length=100)
    total_seats = models.IntegerField()

    def __str__(self):
        return self.name


class Flight(models.Model):
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE)
    departure_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departures')
    arrival_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrivals')

    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()

    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.departure_airport} → {self.arrival_airport}"



class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)

    seat_number = models.CharField(max_length=5)
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.flight}"




# Create your models here.
