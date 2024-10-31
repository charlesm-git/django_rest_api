from rest_framework.viewsets import ModelViewSet

from application.models import Project, Contributor, Issue, Comment
from application.serializers import (
    CommentSerializer,
    ContributorCreationSerializer,
    IssueDetailSerializer,
    IssueListSerializer,
    ProjectListSerializer,
    ProjectDetailSerializer,
)


class MultipleSerializerMixin:
    detail_serializer_class = None

    def get_serializer_class(self):
        if (
            self.action == "retrieve"
            and self.detail_serializer_class is not None
        ):
            return self.detail_serializer_class
        return super().get_serializer_class()


class ProjectViewset(MultipleSerializerMixin, ModelViewSet):
    serializer_class = ProjectListSerializer
    detail_serializer_class = ProjectDetailSerializer
    queryset = Project.objects.all()

    def perform_create(self, serializer):
        project = serializer.save()
        Contributor.objects.create(project=project, contributor=project.author)


class IssueViewset(MultipleSerializerMixin, ModelViewSet):
    serializer_class = IssueListSerializer
    detail_serializer_class = IssueDetailSerializer
    queryset = Issue.objects.all()


class CommentViewset(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class ContributorViewset(ModelViewSet):
    serializer_class = ContributorCreationSerializer
    queryset = Contributor.objects.all()
