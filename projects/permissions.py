from rest_framework import permissions


class IsProjectOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and obj.owner_id == request.user.id
