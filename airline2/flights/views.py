from django.shortcuts import render

from .models import Flight

def index(require):
    return render(require, "flights/index.html", {
        "flights": Flight.objects.all()
    })

def flight(require, flight_id):
    return render(require, "flights/flight.html", {
        "flight": Flight.objects.get(pk=flight_id)
    })
