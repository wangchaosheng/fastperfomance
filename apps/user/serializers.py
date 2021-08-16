from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler


class RegisterSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(label='确认密码', help_text='确认密码', max_length=20, min_length=6,
                                             write_only=True, error_messages={'min_length': '确认密码仅允许6-20个字符',
                                                                              'max_length': '确认密码仅允许6-20个字符'})
    token = serializers.CharField(read_only=True, label='生成token', help_text='生成token')

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'password_confirm', 'token', 'email')
        extra_kwargs = {
            'username': {
                'label': '用户名',
                'help_text': '用户名',
                'max_length': 20,
                'min_length': 6,
                'error_messages': {
                    'min_length': '用户名仅允许6-20个字符',
                    'max_length': '用户名仅允许6-20个字符'
                },
            },
            'password': {
                'label': '密码',
                'help_text': '密码',
                'max_length': 20,
                'min_length': 6,
                'write_only': True,
                'error_messages': {
                    'min_length': '确认密码仅允许6-20个字符',
                    'max_length': '确认密码仅允许6-20个字符'
                }
            },
            'email': {
                'label': '邮箱',
                'help_text': '邮箱',
                'max_length': 30,
                'min_length': 6,
                'write_only': True,
                'required': True,
                'validators': [UniqueValidator(queryset=User.objects.all(), message='此邮箱已注册')]
            }
        }

    def validate(self, attrs):
        if attrs.get('password') != attrs.get('password_confirm'):
            raise serializers.ValidationError('密码与确认密码不一致')
        return attrs

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        # 创建user模型对象
        user = User.objects.create_user(**validated_data)
        # 创建token
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        # 给user模型类对象创建token属性
        user.token = token
        return user
