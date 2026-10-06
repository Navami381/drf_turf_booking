from django.urls import path
from booking_v2.views import SignUpView,TurfBookingListCreateView

urlpatterns=[
    path("signup/",SignUpView.as_view()),
    path("turfbooking/",TurfBookingListCreateView.as_view()),
    
]