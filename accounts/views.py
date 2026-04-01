from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Flight, Booking


# 🏠 Home (simple for now)
@login_required
def home(request):
    return render(request, 'accounts/home.html')

# ✈️ List all flights (no filters yet)
def flight_list(request):
    flights = Flight.objects.all()
    return render(request, 'accounts/flight_list.html', {'flights': flights})


# 🎟️ Book a flight (basic logic)
@login_required
def book_flight(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)

    seat_number = str(flight.booking_set.count() + 1)

    Booking.objects.create(
        user=request.user,
        flight=flight,
        seat_number=seat_number
    )

    messages.success(request, f'Seat booked: {seat_number}')
    return redirect('my_bookings')


# 📄 View bookings
@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'accounts/my_bookings.html', {'bookings': bookings})


# ❌ Cancel booking
@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if request.method == "POST":
        booking.delete()
        messages.success(request, 'Booking cancelled')

    return redirect('my_bookings')