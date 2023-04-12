from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Returns a boolean to see if the user has a read only view or
    if thy are the owner od the post
    """
def has_object_permission(self, request, view, obj):
    if request_method in permission.SAFE_METHODS:
        return True
    return obj.owner == request.user