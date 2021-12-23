from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from utils.makejson import makejson, requestClient, initBoomer, shotdownBoomer, swarm1


@api_view(['GET'])
def request_client(request):
    res = requestClient()
    return Response(res)


@api_view(['POST'])
def init_boomer(request):
    host = request.data.getlist('servAddr[]')

    print(host)
    # res = initBoomer(host)
    return Response('ok')


@api_view(['POST'])
def shutdown_boomer(request):
    host = request.data.getlist('servAddr[]')
    try:
        res = shotdownBoomer(host)
        return Response(res, status=status.HTTP_200_OK)
    except Exception as e:
        res = e
        return Response(res, status=status.HTTP_200_OK)


@api_view(['POST'])
def swarm(request):
    clients = request.data.getlist('client')
    user_count = request.data.getlist('user_count')
    hatch_rate = request.data.getlist('hatch_rate')
    run_time = request.data.getlist('run_time')
    interface_id = request.data.getlist('interface_id')

    res = swarm1(clients, user_count, hatch_rate, run_time,interface_id)

    print(res)
    return Response(res, status=status.HTTP_200_OK)
