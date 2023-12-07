from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """Разрешение на CRUD - автор, остальным чтение."""
    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_staff)


class IsAdminAuthorOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    """Разрешение на CRUD - aминистратор и автор, остальным чтение."""
    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or (request.user == obj.author)
            or request.user.is_staff
        )
