from rest_framework import permissions


class PermissionCuston(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            and request.user.is_superuser
            or request.method not in permissions.SAFE_METHODS
        )
