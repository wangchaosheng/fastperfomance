# -*- coding: utf-8 -*-
# @Time    : 2021/8/18 14:55
# @Author  : qingwu

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.response import Response
from system.models import System
from system.serializers import SystemModelSerializer
from utils.respones import SUCCESS


class SystemViewSets(viewsets.ModelViewSet):
    queryset = System.objects.all()
    serializer_class = SystemModelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset()).exclude(is_delete=1)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(SUCCESS, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        request_obj = System.objects.get(id=request.parser_context.get("kwargs").get("pk"))
        request_obj.is_delete = 1
        request_obj.save()
        return Response(SUCCESS, status=status.HTTP_204_NO_CONTENT)
