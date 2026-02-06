from rest_framework import generics
from rest_framework.permissions import DjangoModelPermissions

from apps.common.models.task import Task
from apps.common.serializers.task import TaskSerializer





class TaskViewMixin:
    permission_classes = []
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TaskListCreateAPI(TaskViewMixin, generics.ListCreateAPIView):
    pass


class TaskDetailsAPI(TaskViewMixin, generics.RetrieveUpdateDestroyAPIView):
    pass
