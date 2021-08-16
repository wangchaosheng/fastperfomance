from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework_jwt.serializers import User

from .serializers import RegisterSerializer


class UserView(CreateAPIView):
    serializer_class = RegisterSerializer


class UsernameIsExist(APIView):

    def get(self, request, username):
        # 数据库查询数量
        count = User.objects.filter(username=username).count()
        # 定义返回字典
        res_dict = {
            'username': username,
            'count': count
        }
        return Response(res_dict)


class EmailIsExist(APIView):

    def get(self, request, email):
        count = User.objects.filter(email=email).count()
        res_dict = {
            'email': email,
            'count': count
        }
        return Response(res_dict)
