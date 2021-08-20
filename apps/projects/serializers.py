from rest_framework import serializers

from projects.models import Projects


class ProjectsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('id', 'system_id', 'name', 'include', 'desc')
