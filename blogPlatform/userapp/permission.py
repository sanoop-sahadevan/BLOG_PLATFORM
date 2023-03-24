# from rest_framework import permissions

# class IsCommentAuthor(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         return obj.user == request.author



from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
    """
    Custom permission to only allow owners of an object to edit or delete it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD, or OPTIONS requests.
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        # Write permissions are only allowed to the owner of the comment.
        return obj.author == request.user
