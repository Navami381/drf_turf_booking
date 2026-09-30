from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from bookings.models import TurfBooking
from bookings.serializers import TurfBookingSerializer
# Create your views here.

class BookingListCreateView(APIView):
    def get(self,request):
        qs=TurfBooking.objects.all()
        serializer_instance=TurfBookingSerializer(qs,many=True)
        return Response(data=serializer_instance.data)