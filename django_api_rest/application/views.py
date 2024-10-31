from rest_framework.viewsets import ModelViewSet

from application.models import Project, Collaborator
from application.serializers import ProjectSerializer


class ProjectViewset(ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    
    def perform_create(self, serializer):
        project = serializer.save()
        Collaborator.objects.create(project=project, collaborator=project.author)
