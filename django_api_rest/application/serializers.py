from rest_framework.serializers import ModelSerializer, CharField

from application.models import Project, Collaborator


class CollaboratorSerializer(ModelSerializer):
    collaborator_name = CharField(source="collaborator.username")

    class Meta:
        model = Collaborator
        fields = ["collaborator_name"]


class ProjectSerializer(ModelSerializer):
    collaborators = CollaboratorSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = [
            "id",
            "name",
            "author",
            "type",
            "date_created",
            "collaborators",
        ]
