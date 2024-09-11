from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Flight, Passenger

def index(request):
    flights = Flight.objects.all()

    return render(request, "flights/index.html", {
        "flights": flights
    })

def flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)

    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all(),
        "no_passengers": Passenger.objects.exclude(flights=flight),
    })

def book(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)

    if request.method == "POST":
        passenger = Passenger.objects.get(pk=request.POST["passenger"])
        passenger.flights.add(flight)
        pass

    return HttpResponseRedirect(reverse("flight", args=[flight_id]))
