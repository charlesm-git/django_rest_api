from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied


class IsAdminOrSelf(BasePermission):

    def has_permission(self, request, view):
        if view.action == "list" and not request.user.is_staff:
            raise PermissionDenied(
                "You must have an admin account to do this action"
            )
        return True

    def has_object_permission(self, request, view, obj):
        if view.action in [
            "retrieve",
            "update",
            "partial_update",
            "destroy",
        ] and (request.user == obj or request.user.is_staff):
            return True
        raise PermissionDenied(
            "You do not have the permission to do this action"
        )
