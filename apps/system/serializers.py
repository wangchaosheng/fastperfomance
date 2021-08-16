from rest_framework import serializers

from system.models import System


class SystemModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = System
        fields = ('id', 'name', 'annotation')
