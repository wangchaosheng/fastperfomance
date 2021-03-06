from django.http import HttpResponse
from django.shortcuts import render
import requests
# Create your views here.
from rest_framework import viewsets, status
from rest_framework.viewsets import GenericViewSet
from interfaces import models, serializers
from interfaces.models import Interfaces
from interfaces.serializers import InterfacesSerializer, InterfacesRunSerializer, InterfacesDebuggingSerializer
from rest_framework.response import Response
from utils.respones import SUCCESS, debug_request
from utils.locustutils import LocustFile, makefile, run
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import action
from utils.makejson import makejson,requestClient,initBoomer
import json
import os
from utils.locustutils import osrun
class InterfaceViewSet(viewsets.ModelViewSet):
    queryset = Interfaces.objects.all()
    serializer_class = InterfacesSerializer
    filter_fields = ['id', 'name', 'path', 'system_id']

    def get_serializer_class(self):
        if self.action == 'run_single':
            return InterfacesRunSerializer
        elif self.action == 'debugging':
            return InterfacesDebuggingSerializer
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
        print("_----------------")
        print(request.data)
        return Response(SUCCESS, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        request_obj = Interfaces.objects.get(id=request.parser_context.get("kwargs").get("pk"))
        request_obj.is_delete = 1
        request_obj.save()
        return Response(SUCCESS, status=status.HTTP_204_NO_CONTENT)

    @action(methods=['post'], detail=True)
    def run_single(self, request, *args, **kwargs):

        try:
            locustapi = Interfaces.objects.get(id=request.parser_context.get("kwargs").get("pk"))

        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializers = self.get_serializer_class()
        serializer = serializers(locustapi)

        qdict = eval(str(serializer.data))
        # .replace(r'"', "")
        # ???????????????,
        # print(qdict)
        # print(type(qdict))
        # api = LocustFile()
        # ?????????????????????????????????????????????
        # datatext = LocustFile.prepare_locust_tests(api, qdict)
        # try:
        #     host = request.data.getlist('servAddr[]')
        #     print(request.data)
        # except Exception as e:
        #     res= e
        #     return Response(res, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        print(request.data)
        print(type(request.data))
        host = request.data.getlist('servAddr[]')
        print(host)
        json1 = makejson(qdict)

        # print(json.dumps(json1,indent=4))
        try:
            res = initBoomer(host,json1)
            return Response(res, status=status.HTTP_200_OK)
        except Exception as e:
            res = e
            return Response(res, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        # ????????????
        # makefile(datatext)
        # ????????????????????????????????????????????????
        # run(datatext)
        # ??????????????????


    @action(methods=['get'], detail=True)
    def debugging(self, request, *args, **kwargs):
        interfaces_obj = Interfaces.objects.get(id=request.parser_context.get("kwargs").get("pk"))
        res = debug_request(interfaces_obj)
        return Response(res, status=status.HTTP_200_OK)
