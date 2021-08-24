from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.viewsets import GenericViewSet
from interfaces_executive_outcomes import models, serializers
from interfaces_executive_outcomes.models import ProjectExecutiveOutcomes
from interfaces_executive_outcomes.serializers import InterfacesExecutiveSerializer
from rest_framework.response import Response
from utils.respones import SUCCESS
from utils.locustutils import LocustFile, makefile, run
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import action

class InterfaceExecutiveViewSet(viewsets.ModelViewSet):
    queryset = ProjectExecutiveOutcomes.objects.all()
    serializer_class = InterfacesExecutiveSerializer
    filter_fields = ['id']


    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(SUCCESS, status=status.HTTP_201_CREATED)