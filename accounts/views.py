from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Flight, Booking
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import Booking
from django.shortcuts import get_object_or_404
from django.db.models import Count
from django.shortcuts import render
from .models import Flight, Booking
from django.contrib import messages

@login_required
def home(request):
    total_flights = Flight.objects.count()
    total_bookings = Booking.objects.filter(user=request.user).count()

    # Popular routes (departure → arrival)
    popular_routes = (
        Booking.objects
        .values('flight__departure_airport__code', 'flight__arrival_airport__code')
        .annotate(count=Count('id'))
        .order_by('-count')[:5]
    )

    # Prepare data for Chart.js
    route_labels = [
        f"{r['flight__departure_airport__code']} → {r['flight__arrival_airport__code']}"
        for r in popular_routes
    ]
    route_counts = [r['count'] for r in popular_routes]

    return render(request, 'accounts/home.html', {
        'total_flights': total_flights,
        'total_bookings': total_bookings,
        'route_labels': route_labels,
        'route_counts': route_counts
    })




def flight_list(request):
    flights = Flight.objects.all()

    departure = request.GET.get('departure')
    arrival = request.GET.get('arrival')
    departure_date = request.GET.get('departure_date')
    arrival_date = request.GET.get('arrival_date')

    if departure:
        flights = flights.filter(departure_airport__code__iexact=departure)
    if arrival:
        flights = flights.filter(arrival_airport__code__iexact=arrival)
    if departure_date:
        flights = flights.filter(departure_time__date=departure_date)
    if arrival_date:
        flights = flights.filter(arrival_time__date=arrival_date)

    return render(request, 'accounts/flight_list.html', {'flights': flights})

@login_required
def book_flight(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)
    # Simple booking logic: assign seat automatically
    seat_number = str(flight.booking_set.count() + 1)
    Booking.objects.create(user=request.user, flight=flight, seat_number=seat_number)
    messages.success(request, f'Flight booked successfully! Seat: {seat_number}')
    return redirect('my_bookings')


@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'accounts/my_bookings.html', {'bookings': bookings})




@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if request.method == "POST":
        booking.delete()
        messages.success(request, f'Booking cancelled successfully.')
    return redirect('my_bookings')

# Create your views here.
