from django.db import models
from app_turf.models import TurfBooking

class Booking(models.Model):

    team_name = models.CharField(max_length=200)

    phone_no = models.CharField(max_length=15)

    turf = models.ForeignKey(TurfBooking,on_delete=models.CASCADE)

    booking_date = models.DateField()

    time = models.TimeField(default="00:00:00")

    duration = models.DurationField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.team_name
