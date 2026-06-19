from django.shortcuts import render


def home(request):
    return render(request, "msresort.html")


def booking(request):
    if request.method == "POST":
        # Showcase mode — show confirmation without saving to database
        return render(request, "success.html")

    return render(request, "booking.html")