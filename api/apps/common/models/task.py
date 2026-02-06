from django.db import models

from apps.common.models.priority import Priority


class Task(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    start = models.DateField()
    end = models.DateField()
    priority = models.CharField(
        max_length=50,
        choices=Priority.choices,
        default=Priority.MEDIUM,
        blank=False,
        null=False,
    )
    completed = models.BooleanField(default=False)
