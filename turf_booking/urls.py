"""
URL configuration for turf_booking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_turf.views import TurfListCreteView,TurfRetrieveUpdateDeleteView,AdminRegisterView
from bookings.views import BookingListCreateView,BookingRetriveUpdateDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("turf/",TurfListCreteView.as_view()),
    path("turf/<int:pk>/",TurfRetrieveUpdateDeleteView.as_view()),

    #admin register
    path("admin_register/",AdminRegisterView.as_view()),

    #bookings
    path("bookings/",BookingListCreateView.as_view()),
    path("bookings/<int:pk/",BookingRetriveUpdateDeleteView.as_view()),
    
]
