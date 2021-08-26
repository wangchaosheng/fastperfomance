from rest_framework import serializers

from execute_logs.models import ExecuteLogs


class ExecuteLogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExecuteLogs
        fields = '__all__'