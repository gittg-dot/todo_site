from django.db import models

from apps.common.models.task import Task




class Project(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    tasks = models.ForeignKey(Task, related_name="tasks", on_delete=models.CASCADE)