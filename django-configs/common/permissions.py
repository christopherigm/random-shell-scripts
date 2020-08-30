from rest_framework.permissions import BasePermission

class IsAdminOrIsItSelf(BasePermission):
  def has_object_permission(self, request, view, obj):
    return(
      (obj==request.user) or (request.user.is_superuser)
    )

class IsSuperUser(BasePermission):
  def has_permission(self, request, view):
    return request.user.is_superuser


class IsAdminOrBelongsToItSelf(BasePermission):
  def has_object_permission(self, request, view, obj):
    return(
      (obj.user==request.user) or (request.user.is_superuser)
    )