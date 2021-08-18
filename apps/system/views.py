from rest_framework import viewsets

from system.models import System
from system.serializers import SystemModelSerializer


class SystemViewSets(viewsets.ModelViewSet):
    queryset = System.objects.all()
    serializer_class = SystemModelSerializer
