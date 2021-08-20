# -*- coding: utf-8 -*-
# @Time    : 2021/8/20 14:55
# @Author  : qingwu

from rest_framework import viewsets, status
from rest_framework.response import Response
from projects.models import Projects
from projects.serializers import ProjectsModelSerializer
from utils.respones import SUCCESS


class ProjectsViewSets(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsModelSerializer
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
        request_obj = Projects.objects.get(id=request.parser_context.get("kwargs").get("pk"))
        request_obj.is_delete = 1
        request_obj.save()
        return Response(SUCCESS, status=status.HTTP_204_NO_CONTENT)
