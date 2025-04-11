from django.db import models
from django.contrib.auth.models import User
from movies.models import Movie

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    booking_date = models.DateField()
    tickets = models.IntegerField()

    def __str__(self):
        return f"Booking {self.id} for {self.user.username}"


# Create your models here.
