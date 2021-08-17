from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from .serializers import RegisterSerializer


class UserView(CreateAPIView):
    serializer_class = RegisterSerializer


class UsernameIsExistedView(APIView):

    def get(self, request, username):
        count = User.objects.filter(username=username).count()
        one_dict = {
            'username': username,
            'count': count
        }

        return Response(one_dict)


class EmailIsExistedView(APIView):

    def get(self, request, email):
        count = User.objects.filter(email=email).count()
        one_dict = {
            'email': email,
            'count': count
        }

        return Response(one_dict)
