from django.db import models
from django.conf import settings
import uuid


class Project(models.Model):
    FRONTEND = "Front-end"
    BACKEND = "Back-end"
    ANDROID = "Android"
    IOS = "iOS"

    TYPE_CHOICES = [
        (FRONTEND, "Front-end"),
        (BACKEND, "Back-end"),
        (ANDROID, "Android"),
        (IOS, "iOS"),
    ]

    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    date_created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=15, choices=TYPE_CHOICES)


class Collaborator(models.Model):
    project = models.ForeignKey(
        to=Project, on_delete=models.CASCADE, related_name="collaborators"
    )
    collaborator = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="collaborations",
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["project", "collaborator"],
                name="unique_project_collaborator",
            )
        ]
