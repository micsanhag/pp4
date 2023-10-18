from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .models import Booking

@login_required
def bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings.html', {'bookings': bookings})

@login_required
def cancel_booking(request, id):
    booking = Booking.objects.get(id=id)
    booking.delete()
    return HttpResponseRedirect('bookings')

