from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import UserSerializer, BookingSerializer, MenuSerializer
from .models import Booking, Menu
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from rest_framework.decorators import api_view
# Create your views here.


class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    
class MenuView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer   


class BookingViewSet(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    
    

@api_view(['GET', 'POST'])  
def new_user(request):
    
    username = request.GET.get('username')
    password = request.GET.get('password')
    