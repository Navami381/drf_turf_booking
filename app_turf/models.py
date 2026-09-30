from django.db import models

# Create your models here.
class TurfBooking(models.Model):
    name=models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    phone_no=models.PositiveIntegerField()
    fee=models.PositiveIntegerField()
