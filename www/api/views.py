from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from api.serializers import *
from crms.models import *
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows to be viewed or edited
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows to be viewed or edited
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class CarViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows to be viewed or edited
    """
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class OfferViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows to be viewed or edited
    """
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

class DealViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows to be viewed or edited
    """
    queryset = Deal.objects.all()
    serializer_class = DealSerializer
