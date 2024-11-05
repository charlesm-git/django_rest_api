from rest_framework.serializers import (
    ModelSerializer,
    CharField,
    IntegerField,
    PrimaryKeyRelatedField,
    ValidationError,
)

from application.models import Comment, Issue, Project, Contributor
from users.models import User


class ContributorSerializer(ModelSerializer):
    """Serializer used to present the contributors of a project"""

    contributor_name = CharField(source="contributor.username")
    contributor_id = IntegerField(source="contributor.id")

    class Meta:
        model = Contributor
        fields = ["id", "contributor_id", "contributor_name"]


class ContributorCreationSerializer(ModelSerializer):
    """
    Serializer used when the contributor url is called to be able to
    create one
    """

    class Meta:
        model = Contributor
        fields = [
            "id",
            "project",
            "contributor",
        ]


class CommentSerializer(ModelSerializer):
    """Main Comment serialiazer"""

    author = PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = [
            "id",
            "issue",
            "author",
            "description",
            "date_created",
            "uuid",
        ]


class BaseIssueSerializer(ModelSerializer):
    """
    Base Serializer for Issue Model that implement the validate_attribution
    method
    """

    author = PrimaryKeyRelatedField(read_only=True)

    def validate_attribution(self, value):
        project = self.initial_data.get("project") or self.instance.project
        if not Contributor.objects.filter(
            project=project, contributor=value
        ).exists():
            raise ValidationError(
                "The attributed user must be a contributor to the project."
            )
        return value


class IssueListSerializer(BaseIssueSerializer):
    """List view Issue Serializer"""

    class Meta:
        model = Issue
        fields = [
            "id",
            "project",
            "name",
            "author",
            "description",
            "status",
            "priority",
            "tag",
            "attribution",
            "date_created",
        ]


class IssueDetailSerializer(BaseIssueSerializer):
    """
    Detail view Issue serialiazer. Adds the associated comments compared to the
    list serializer
    """

    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Issue
        fields = [
            "id",
            "project",
            "name",
            "author",
            "description",
            "status",
            "priority",
            "tag",
            "attribution",
            "date_created",
            "comments",
        ]


class ProjectListSerializer(ModelSerializer):
    """List view project serializer"""

    author = PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Project
        fields = [
            "id",
            "name",
            "author",
            "type",
            "description",
            "date_created",
        ]


class ProjectDetailSerializer(ModelSerializer):
    """
    Detail view project serializer. Adds the display of the contributors and
    issues (without comments) compared to the list serializer.
    """

    author = PrimaryKeyRelatedField(read_only=True)
    contributors = ContributorSerializer(many=True, read_only=True)
    issues = IssueListSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = [
            "id",
            "name",
            "author",
            "type",
            "date_created",
            "contributors",
            "issues",
        ]
