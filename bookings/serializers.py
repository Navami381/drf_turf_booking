from rest_framework import serializers

class TurfBookingSerializer(serializers.Serializer):
    team_name=serializers.CharField()
    phone_no=serializers.IntegerField()
    booking_date=serializers.DateField()
    turf=serializers.IntegerField()
    time=serializers.TimeField()
    duration=serializers.DurationField()
    