from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response

from app_turf.models import TurfBooking
from app_turf.serilaizers import TurfSerializer,UserSerializer

from rest_framework import authentication,permissions

# Create your views here.
class TurfListCreteView(APIView):

    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAdminUser]

    def get(self,request):
        qs=TurfBooking.objects.all()
        serializer_instance=TurfSerializer(qs,many=True)
        return Response(data=serializer_instance.data)

    def post(self,request):
        form_data=request.data
        serializer_instance=TurfSerializer(data=form_data)
        if serializer_instance.is_valid():
            cleaned_data=serializer_instance.validated_data
            TurfBooking.objects.create(**cleaned_data)
            return Response(data=serializer_instance.validated_data)
        else:
            return Response(data=serializer_instance.errors)
        
class TurfRetrieveUpdateDeleteView(APIView):
    def get(self,request,pk=None):
        qs=TurfBooking.objects.get(id=pk)
        serilaizer_instance=TurfSerializer(qs)
        return Response(data=serilaizer_instance.data)

    def put(self,request,pk=None):
        form_data=request.data
        serializer_instance=TurfSerializer(data=form_data)
        if serializer_instance.is_valid():
            cleaned_data=serializer_instance.validated_data
            TurfBooking.objects.filter(id=pk).update(**cleaned_data)
            return Response(data=serializer_instance.validated_data)
        else:
            return Response(data=serializer_instance.errors)

    def delete(self,request,pk=None):
        qs=TurfBooking.objects.get(id=pk).delete()
        return Response(data={"message":"deleted.."})

class AdminRegisterView(APIView):
    def post(self,request):
        form_data=request.data
        serializer_instance=UserSerializer(data=form_data)
        if serializer_instance.is_valid():
            cleaned_data=serializer_instance.validated_data
            
            User.objects.create_superuser(**cleaned_data)
            return Response(data=serializer_instance.validated_data)
        else:
             return Response(data=serializer_instance.errors)