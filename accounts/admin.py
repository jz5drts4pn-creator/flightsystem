from django.contrib import admin
from .models import Airport, Aircraft, Flight, Booking

@admin.register(Airport)
class AirportAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'city', 'country')
    search_fields = ('code', 'name', 'city', 'country')

@admin.register(Aircraft)
class AircraftAdmin(admin.ModelAdmin):
    list_display = ('name', 'total_seats')

@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ('departure_airport', 'arrival_airport', 'departure_time', 'arrival_time', 'price')
    list_filter = ('departure_airport', 'arrival_airport')
    search_fields = ('departure_airport__code', 'arrival_airport__code')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'flight', 'seat_number', 'booked_at')
    list_filter = ('flight',)
    search_fields = ('user__username', 'flight__departure_airport__code', 'flight__arrival_airport__code')


class BookingInline(admin.TabularInline):
    model = Booking
    extra = 0


# Register your models here.
