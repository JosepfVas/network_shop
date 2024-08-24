from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser


class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user and (request.user.is_superuser or obj == request.user)


class IsActiveEmployee(BasePermission):
    """
    Разрешение для проверки, что пользователь активен и является сотрудником.
    """

    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.is_active
            and request.user.is_staff
        )
