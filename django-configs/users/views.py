from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from common.permissions import (
  IsAdminOrIsItSelf,
  IsSuperUser,
  IsAdminOrBelongsToItSelf
)
from django.contrib.auth.models import User, Group
from users.models import UserAddress
from users.serializers import (
  GroupSerializer,
  UserSerializer,
  UserAddressSerializer
)
from common.mixins import (
  BTUCreate,
  BTUUpdate
)

# Create your views here.

class GroupViewSet (
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet
  ):
  queryset = Group.objects.all()
  serializer_class = GroupSerializer
  ordering = ['id']
  permission_classes = [ IsAuthenticated ]
  authentication_classes = [
    JWTAuthentication,
    SessionAuthentication
  ]
  ordering_fields = [ 'id', 'name' ]
  filterset_fields = {
    'id': ('exact',),
    'name': ('exact', 'in')
  }
  search_fields = [
    'name'
  ]

class UserViewSet(ModelViewSet):
  """
  User instance
  """
  queryset = User.objects.all()
  serializer_class = UserSerializer
  ordering = ['id']
  permission_classes = [ IsAuthenticated ]
  authentication_classes = [
    JWTAuthentication,
    SessionAuthentication
  ]
  ordering_fields = [
    'id', 'first_name', 'last_name', 'last_login'
  ]
  filterset_fields = {
    'id': ('exact',),
    'is_superuser': ('exact',),
    'username': ('exact', 'in'),
    'email': ('exact', 'in'),
    'last_login': ('exact', 'lt', 'gt', 'gte', 'lte', 'in'),
    'date_joined': ('exact', 'lt', 'gt', 'gte', 'lte', 'in')
  }
  search_fields = [
    'first_name', 'last_name', 'email', 'username'
  ]

  def get_permissions(self):
    permission_classes = [IsAdminOrIsItSelf]
    if self.action in ('list','destroy'):
      permission_classes = [IsSuperUser]
    if self.action == 'create':
      permission_classes = []

    return [permission() for permission in permission_classes]


class UserAddressViewSet (
      BTUCreate,
      BTUUpdate,
      mixins.ListModelMixin,
      mixins.RetrieveModelMixin,
      mixins.DestroyModelMixin,
      GenericViewSet
    ):
    """
    User Address Instance
    """
    queryset = UserAddress.objects.all()
    serializer_class = UserAddressSerializer
    ordering = ['id']
    permission_classes = [ 
      IsAuthenticated,
      IsAdminOrBelongsToItSelf
    ]
    authentication_classes = [
      JWTAuthentication,
      SessionAuthentication
    ]
    ordering_fields = [
      'id', 'alias'
    ]
    filterset_fields = {
      'enabled': ('exact',),
      'id': ('exact', 'lt', 'gt', 'gte', 'lte'),
      'created': ('exact', 'lt', 'gt', 'gte', 'lte', 'in'),
      'modified': ('exact', 'lt', 'gt', 'gte', 'lte', 'in'),
      'zip_code': ('exact',)
    }
    search_fields = [
      'alias', 'receptor_name', 'phone',
      'zip_code', 'street'
    ]

    def get_queryset(self):
      user = self.request.user
      if not user.is_anonymous and not user.is_superuser:
        return UserAddress.objects.filter(user=user)
      return UserAddress.objects.all()
