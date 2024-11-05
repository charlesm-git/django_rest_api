from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied

from application.models import Contributor, Issue, Project

CREATE_METHOD = ["POST"]
UPDATE_METHOD = ["PUT", "PATCH", "DELETE"]


class IsContributor(BasePermission):
    """
    Only contributors to a project can create Issues, Comments and Contributors
    """

    def has_permission(self, request, view):
        if request.method in CREATE_METHOD:
            # In case of an Issue or a Contributor creation, get the project
            # ID from the data given
            project_id = request.data.get("project")
            # In case of a Comment, get the project ID after fetching the
            # related issue's data
            if not project_id and "issue" in request.data:
                issue_id = request.data.get("issue")
                issue = Issue.objects.filter(pk=issue_id).first()
                if issue is not None:
                    project_id = issue.project.id
                else:
                    PermissionDenied("Invalid Issue reference")

            # If a project with this id exists, checks if the user is a
            # contributor and return a granted permission or an error
            if project_id:
                project = Project.objects.filter(pk=project_id).first()
                if project is not None:
                    if Contributor.objects.filter(
                        project=project, contributor=request.user
                    ).exists():
                        return True
                    else:
                        raise PermissionDenied(
                            "You must be a contributor to the project to "
                            "perform this action"
                        )
                else:
                    raise PermissionDenied("Invalid project reference")
            else:
                raise PermissionDenied("Project or issue ID is required")
        else:
            return True


class IsAuthorToModify(BasePermission):
    """
    Object permission : Only the author of an object can modify and delete it
    """

    def has_object_permission(self, request, view, obj):
        if request.method in UPDATE_METHOD:
            if obj.author == request.user:
                return True
            else:
                raise PermissionDenied(
                    "You must be the author of this post to do this action"
                )
        return True
