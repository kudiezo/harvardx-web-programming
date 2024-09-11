from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Flight, Passenger

def index(require):
    return render(require, "flights/index.html", {
        "flights": Flight.objects.all()
    })

def flight(require, flight_id):
    flight = Flight.objects.get(pk=flight_id)

    return render(require, "flights/flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all(),
        "no_passengers": Passenger.objects.exclude(flights=flight),
    })

def book(require, flight_id):
    flight = Flight.objects.get(pk=flight_id)

    if require.method == "POST":
        passenger = Passenger.objects.get(pk=int(require.POST["passenger"]))
        passenger.flights.add(flight)
    return HttpResponseRedirect(reverse("flight", args=[flight_id]))
