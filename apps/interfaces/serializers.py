from rest_framework import serializers

from interfaces.models import Interfaces


class InterfacesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interfaces
        fields = '__all__'


class InterfacesRunSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interfaces
        fields = ('request', 'path', 'method', 'threads', 'rate', 'execution_time', 'assertstr', 'is_delete')


class InterfacesDebuggingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interfaces
        fields = ('id',)
