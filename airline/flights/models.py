from django.db import models

class Airport(models.Model):
    city = models.CharField(max_length=64)
    code = models.CharField(max_length=3)

    def __str__(self) -> str:
        return f"{self.city} ({self.code})"
    pass

class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departure")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrival")
    duration = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.origin} to {self.destination}"
    
    def is_flight_valid(self):
        return self.origin != self.destination and self.duration > 0

class Passenger(models.Model):
    first = models.CharField(max_length=24)
    last = models.CharField(max_length=24)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")

    def __str__(self) -> str:
        return f"{self.first} {self.last}"
    pass


