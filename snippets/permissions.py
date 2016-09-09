#Object Level Permissions
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """Custom permission to only allow owners of an object to modify it
    """

    def has_object_permission(self,request,view,obj):
        #Read permissions always allow GET,HEAD or OPTIONS
        if request.method in permissions.SAFE_METHODS:
            return True


        #Write permissions are only allowed for owner of the snippet.
        return obj.owner == request.user


