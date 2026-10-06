from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response

from booking_v2.serializers import SignUpSerializer,TurfBookingSerializer
from booking_v2.models import BookingV2

from datetime import time,datetime,timedelta

# Create your views here.
class SignUpView(APIView):

    def post(self,request):

        form_data=request.data
        serializer_instance=SignUpSerializer(data=form_data)
        if serializer_instance.is_valid():
            cleaned_data=serializer_instance.validated_data
            user_object=User.objects.create_user(**cleaned_data)
            serializer_instance=SignUpSerializer(user_object)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)
    
     
class TurfBookingListCreateView(APIView):
    def get(self,request):
        qs=BookingV2.objects.all()
        serializer_instance=TurfBookingSerializer(qs,many=True)
        return Response(data=serializer_instance.data)

    def post(self,request):
        form_data=request.data
        serializer_instance=TurfBookingSerializer(data=form_data)
        if serializer_instance.is_valid():
            cleaned_data=serializer_instance.validated_data
            turf_id=cleaned_data.get("turf")
            booking_date=cleaned_data.get("booking_date")
            booking_time=time(10,0)
            duration = timedelta(hours=2)

            last_booking_object=BookingV2.objects.filter(turf=turf_id,booking_date=booking_date).last()
            if last_booking_object:
                next_booking_date_time=datetime.combine(booking_date,last_booking_object.booking_time)+duration
                booking_time=next_booking_date_time.time()
                           
            else: 
                booking_time = time(10,0)

            end_time =(datetime.combine(booking_date,booking_time) + duration).time()            
            qs=BookingV2.objects.create(**cleaned_data,booking_time=booking_time,end_time=end_time,duration=duration)
            serializer_instance=TurfBookingSerializer(qs)
            return Response(data=serializer_instance.data)
        else:
                return Response(data=serializer_instance.errors)

    
    
