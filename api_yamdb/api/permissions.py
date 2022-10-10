from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAdmin(BasePermission):
    """
    Allows access only admins or superusers to everything.
    """

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.is_admin or request.user.is_superuser
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            return request.user.is_admin or request.user.is_superuser
        else:
            return False


class IsSelf(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return all([request.user.is_authenticated, request.user == obj])


class IsAuthorModeratorAdminOrReadOnly(BasePermission):
    def has_permissions(self, request, view):
        return request.method in SAFE_METHODS or request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return (
            request.method in SAFE_METHODS
            or request.method == 'POST'
            and request.user.is_authenticated
            or obj.author == request.user
            or request.user.is_admin
            or request.user.is_moderator
        )


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.is_admin or request.user.is_superuser
        return request.method in SAFE_METHODS
