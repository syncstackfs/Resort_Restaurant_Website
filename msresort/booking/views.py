from django.shortcuts import render
from .models import Booking


def home(request):
    return render(request, "msresort.html")


def booking(request):
    if request.method == "POST":
        try:
            Booking.objects.create(
                name=request.POST.get("name"),
                email=request.POST.get("email"),
                phone=request.POST.get("phone"),
                room=request.POST.get("room"),
                checkin=request.POST.get("checkin"),
                checkout=request.POST.get("checkout"),
                guests=int(request.POST.get("guests")),
            )

            return render(request, "success.html")

        except Exception as e:
            return render(
                request,
                "booking.html",
                {
                    "error": f"Booking failed: {e}"
                },
            )

    return render(request, "booking.html")
