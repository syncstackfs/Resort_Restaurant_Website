from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    room = models.CharField(max_length=100)
    checkin = models.DateField()
    checkout = models.DateField()
    guests = models.IntegerField()

    def __str__(self):
        return self.name
