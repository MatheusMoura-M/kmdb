from rest_framework import permissions


class IsFreeForReading(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.method not in permissions.SAFE_METHODS
            and request.user.is_superuser
        )
