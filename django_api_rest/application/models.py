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

    def __str__(self):
        return self.name


class Issue(models.Model):
    TO_DO = "To Do"
    IN_PROGRESS = "In Progress"
    FINISHED = "Finished"

    STATUS_LIST = [
        (TO_DO, "To Do"),
        (IN_PROGRESS, "In Progress"),
        (FINISHED, "Finished"),
    ]

    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"

    PRIORITY_LIST = [
        (LOW, "Low"),
        (MEDIUM, "Medium"),
        (HIGH, "High"),
    ]

    BUG = "Bug"
    FEATURE = "Feature"
    TASK = "Task"

    TAG_LIST = [
        (BUG, "Bug"),
        (FEATURE, "Feature"),
        (TASK, "Task"),
    ]

    project = models.ForeignKey(
        to=Project, on_delete=models.CASCADE, related_name="issues"
    )
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=1024)
    status = models.CharField(
        max_length=15, choices=STATUS_LIST, default=TO_DO
    )
    priority = models.CharField(max_length=8, choices=PRIORITY_LIST, default=LOW)
    tag = models.CharField(max_length=8, choices=TAG_LIST)
    attribution = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="attributed_issues",
        null=True,
    )
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    description = models.TextField(max_length=1024)
    date_created = models.DateTimeField(auto_now_add=True)
    issue = models.ForeignKey(
        to=Issue, on_delete=models.CASCADE, related_name="comments"
    )
    uuid = models.UUIDField(
        primary_key=False, default=uuid.uuid4, editable=False
    )


class Contributor(models.Model):
    """Intermediate model to make the link between a Project and a User"""

    project = models.ForeignKey(
        to=Project, on_delete=models.CASCADE, related_name="contributors"
    )
    contributor = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="contributions",
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["project", "contributor"],
                name="unique_project_contributor",
            )
        ]
