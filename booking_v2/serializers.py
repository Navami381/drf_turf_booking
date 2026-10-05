from rest_framework import serializers

from booking_v2.models import BookingV2

from django.contrib.auth.models import User



class SignUpSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields=["username","email","password"]

class TurfBookingSerializer(serializers.ModelSerializer):

    class Meta:
        model=BookingV2
        fields="__all__"
        read_only_fields = ["end_time", "created_at"]
