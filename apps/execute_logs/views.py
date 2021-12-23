

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.response import Response
from execute_logs.models import ExecuteLogs
from execute_logs.serializers import ExecuteLogsSerializer
from utils.respones import SUCCESS

class ExecuteLogViewSets(viewsets.ModelViewSet):
    queryset = ExecuteLogs.objects.all()
    serializer_class = ExecuteLogsSerializer
    # filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id']

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset()).exclude(is_delete=1)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        data = {
            'execute_logs_id':response.data['id'],
            'interface_id':response.data['interface_id'],
            'msg': 'success',
            'status': 0}
        return Response(data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response(SUCCESS, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        request_obj = ExecuteLogs.objects.get(id=request.parser_context.get("kwargs").get("pk"))
        request_obj.is_delete = 1
        request_obj.save()
        return Response(SUCCESS, status=status.HTTP_204_NO_CONTENT)