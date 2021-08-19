from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from interfaces.models import Interfaces
from interfaces.serializers import InterfacesSerializer


class InterfaceViewSet(viewsets.ModelViewSet):
    queryset = Interfaces.objects.all()
    serializer_class = InterfacesSerializer