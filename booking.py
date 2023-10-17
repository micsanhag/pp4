from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .models import Restaurant, Booking

@login_required
def book_table(request):
    if request.method == 'POST':
        restaurant = Restaurant.objects.get(id=request.POST['restaurant'])
        date = request.POST['date']
        time = request.POST['time']
        number_of_guests = request.POST['number_of_guests']
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']

        booking = Booking.objects.create(
            restaurant=restaurant,
            date=date,
            time=time,
            number_of_guests=number_of_guests,
            name=name,
            email=email,
            phone_number=phone_number,
        )

        return HttpResponseRedirect('booking_confirmation', booking.id)

    restaurants = Restaurant.objects.all()
    return render(request, 'book_table.html', {'restaurants': restaurants})

@login_required
def booking_confirmation(request, id):
    booking = Booking.objects.get(id=id)
    return render(request, 'booking_confirmation.html', {'booking': booking})
