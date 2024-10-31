from rest_framework.serializers import (
    ModelSerializer,
    CharField,
    ValidationError,
)

from application.models import Comment, Issue, Project, Contributor


class ContributorSerializer(ModelSerializer):
    name = CharField(source="contributor.username")
    id = CharField(source="contributor.id")

    class Meta:
        model = Contributor
        fields = ["id", "name"]


class ContributorCreationSerializer(ModelSerializer):
    contributor_id = CharField(source="contributor.id")
    contributor_name = CharField(source="contributor.username", read_only=True)
    project_id = CharField(source="project.id")
    project_name = CharField(source="project.name", read_only=True)

    class Meta:
        model = Contributor
        fields = ["contributor_id", "contributor_name", "project_id", "project_name"]


class CommentSerializer(ModelSerializer):

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


class IssueListSerializer(ModelSerializer):

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

    def validate_attribution(self, value):
        project = self.initial_data.get("project")
        if not Contributor.objects.filter(
            project=project, contributor=value
        ).exists():
            raise ValidationError(
                "The attributed user must be a contributor to the project."
            )
        return value


class IssueDetailSerializer(ModelSerializer):
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

    def validate_attribution(self, value):
        project = self.initial_data.get("project")
        if not Contributor.objects.filter(
            project=project, contributor=value
        ).exists():
            raise ValidationError(
                "The attributed user must be a contributor to the project."
            )
        return value


class ProjectListSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = [
            "id",
            "name",
            "author",
            "type",
            "date_created",
        ]


class ProjectDetailSerializer(ModelSerializer):
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
