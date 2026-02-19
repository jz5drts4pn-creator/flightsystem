"""
URL configuration for flightproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

from django.shortcuts import render
from accounts.models import Flight, Booking
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    total_flights = Flight.objects.count()
    total_bookings = Booking.objects.filter(user=request.user).count()
    return render(request, 'accounts/home.html', {
        'total_flights': total_flights,
        'total_bookings': total_bookings
    })






urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('users/', include('users.urls')),
    path('accounts/', include('accounts.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
]
