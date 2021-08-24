from rest_framework import serializers

from interfaces_executive_outcomes.models import ProjectExecutiveOutcomes


class InterfacesExecutiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectExecutiveOutcomes
        fields = '__all__'