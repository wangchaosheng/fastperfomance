from rest_framework import serializers

from system.models import System


class SystemModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = System
        exclude = ('update_time', 'create_time')
