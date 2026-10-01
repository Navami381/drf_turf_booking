from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from bookings.models import Booking
from bookings.serializers import TurfBookingSerializer

from app_turf.models import TurfBooking
# Create your views here.

class BookingListCreateView(APIView):
    def get(self,request):
        qs=Booking.objects.all()
        serializer_instance=TurfBookingSerializer(qs,many=True)
        return Response(data=serializer_instance.data)

    def post(self, request):
        form_data = request.data
        serializer_instance = TurfBookingSerializer(data=form_data)
        if serializer_instance.is_valid():
            cleaned_data = serializer_instance.validated_data
            """
            cleaned_data = {

                "team_name": "Thunder Strikers",
                "phone_no": "9876543210",
                "booking_date": "2026-10-10",
                "turf": 3,
                "time": "18:00:00",
                "duration": "02:00:00"
            }
            """
            turf = cleaned_data.get("turf")   # turf_id
            turf_object = TurfBooking.objects.get(id=turf)
            cleaned_data["turf"] = turf_object
            Booking.objects.create(**cleaned_data)

            response_data = {
                "status": "booked"
            }
            return Response(data=response_data)
        else:
            return Response(data=serializer_instance.errors)

class BookingRetriveUpdateDeleteView(APIView):
    def get(self,request,pk=None):
            qs=Booking.objects.get(id=pk)
            serilaizer_instance=TurfBookingSerializer(qs)
            return Response(data=serilaizer_instance.data)

    def put(self,request,pk=None):
            form_data=request.data
            serializer_instance=TurfBookingSerializer(data=form_data)
            if serializer_instance.is_valid():
                cleaned_data=serializer_instance.validated_data
                Booking.objects.filter(id=pk).update(**cleaned_data)
                return Response(data=serializer_instance.validated_data)
            else:
                return Response(data=serializer_instance.errors)

    def delete(self,request,pk=None):
            qs=Booking.objects.get(id=pk).delete()
            return Response(data={"message":"deleted.."})
    