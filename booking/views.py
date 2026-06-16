from django.shortcuts import render
from .models import Booking


def home(request):
    return render(request, "msresort.html")


def booking(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        room = request.POST.get("room")
        checkin = request.POST.get("checkin")
        checkout = request.POST.get("checkout")
        guests = request.POST.get("guests")

        Booking.objects.create(
            name=name,
            email=email,
            phone=phone,
            room=room,
            checkin=checkin,
            checkout=checkout,
            guests=guests
        )

        return render(request, "success.html")

    return render(request, "booking.html")