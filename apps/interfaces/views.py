from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.viewsets import GenericViewSet
from interfaces import models, serializers
from interfaces.models import Interfaces
from interfaces.serializers import InterfacesSerializer, InterfacesRunSerializer
from rest_framework.response import Response
from utils.respones import SUCCESS
from utils.locustutils import LocustFile, makefile, run
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import action



class InterfaceViewSet(viewsets.ModelViewSet):
    queryset = Interfaces.objects.all()
    serializer_class = InterfacesSerializer
    filter_fields = ('id', 'name', 'path', 'system_id')

    def get_serializer_class(self):
        if self.action == 'run_single':
            return InterfacesRunSerializer
        else:
            return self.serializer_class

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
        request_obj = Interfaces.objects.get(id=request.parser_context.get("kwargs").get("pk"))
        request_obj.is_delete = 1
        request_obj.save()
        return Response(SUCCESS, status=status.HTTP_204_NO_CONTENT)

    @action(methods=['get'], detail=True)
    def run_single(self, request, *args, **kwargs):
        try:
            locustapi = Interfaces.objects.get(id=request.parser_context.get("kwargs").get("pk"))
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializers = self.get_serializer_class()
        serializer = serializers(locustapi)

        qdict = eval(str(serializer.data))
        # .replace(r'"', "")
        # 去掉所有的,
        # print(qdict)
        # print(type(qdict))
        api = LocustFile()
        # 生成了一个类对象去接收各个属性
        datatext = LocustFile.prepare_locust_tests(api, qdict)
        # 接受属性
        makefile(datatext)
        # 把替换好的对象传进去的到文件地址
        run(datatext)
        # 给对象和属性
        return Response(status=status.HTTP_200_OK)
