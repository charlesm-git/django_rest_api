from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from application.models import Project, Contributor, Issue, Comment
from application.serializers import (
    CommentSerializer,
    ContributorCreationSerializer,
    IssueDetailSerializer,
    IssueListSerializer,
    ProjectListSerializer,
    ProjectDetailSerializer,
)
from application.permissions import IsAuthorToModify, IsContributor


class MultipleSerializerMixin:
    """
    Mixin to have multiple serializers.
    Allow the possibility to use a detail serializer for an object specific
    view.
    """

    detail_serializer_class = None

    def get_serializer_class(self):
        if (
            self.action == "retrieve"
            and self.detail_serializer_class is not None
        ):
            return self.detail_serializer_class
        return super().get_serializer_class()


class ProjectViewset(MultipleSerializerMixin, ModelViewSet):
    """
    Viewset for the model Project.
    Use 2 serializers, one for the list view and one for the detail view.
    """

    serializer_class = ProjectListSerializer
    detail_serializer_class = ProjectDetailSerializer
    # The User needs to be identify to create a project and he is the only one
    # that can update/delete it
    permission_classes = [IsAuthenticated, IsAuthorToModify]

    def get_queryset(self):
        """The user can only access the projects where he is a contributor."""
        user = self.request.user
        return Project.objects.filter(contributors__contributor=user)

    def perform_create(self, serializer):
        """Add the author as a contributor when a project is created"""
        project = serializer.save(author=self.request.user)
        Contributor.objects.create(project=project, contributor=project.author)


class IssueViewset(MultipleSerializerMixin, ModelViewSet):
    """
    Viewset for the model Issue
    Use 2 serializers, one for the list view and one for the detail view
    """

    serializer_class = IssueListSerializer
    detail_serializer_class = IssueDetailSerializer
    # The User needs to be identified and a contributor to the project to be
    # able to create an Issue, he is the only one that can update/delete it
    permission_classes = [
        IsAuthenticated,
        IsContributor,
        IsAuthorToModify,
    ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        """
        The user can only access the issues from projects where he is a
        contributor himself.
        """
        user = self.request.user
        return Issue.objects.filter(project__contributors__contributor=user)


class CommentViewset(ModelViewSet):
    """Viewset for the model Comment"""

    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    # The User needs to be identified and a contributor to the ptoject to be
    # able to create a Comment, he is the only one that can update/delete it
    permission_classes = [
        IsAuthenticated,
        IsContributor,
        IsAuthorToModify,
    ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        """
        The user can only access the comments from projects where he is a
        contributor himself.
        """
        user = self.request.user
        return Comment.objects.filter(
            issue__project__contributors__contributor=user
        )


class ContributorViewset(ModelViewSet):
    """Viewset for the model Contributor"""

    serializer_class = ContributorCreationSerializer
    # The User need to be identified and a contributor to the project to be
    # able to add/update/delete another contributor
    permission_classes = [IsAuthenticated, IsContributor]

    def get_queryset(self):
        """
        The user can only access the contributors from projects where he is a
        contributor himself.
        """
        user = self.request.user
        return Contributor.objects.filter(
            project__contributors__contributor=user
        )
