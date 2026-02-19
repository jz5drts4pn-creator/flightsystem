from django.urls import path
from . import views

urlpatterns = [
    path('flights/', views.flight_list, name='flight_list'),
    path('flights/book/<int:flight_id>/', views.book_flight, name='book_flight'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('bookings/cancel/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
    path('', views.home, name='home'),
]
