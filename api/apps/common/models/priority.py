from django.db import models


class Priority(models.TextChoices):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"