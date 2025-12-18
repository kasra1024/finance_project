from rest_framework.permissions import BasePermission , AllowAny

class IsAdminUserCustom(BasePermission) : 
    def has_permission(self, request, view):
        return request.user 
    

class IsOwner(BasePermission) : 
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
    