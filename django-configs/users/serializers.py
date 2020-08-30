from rest_framework_json_api import serializers
from rest_framework_json_api.serializers import HyperlinkedModelSerializer
from rest_framework.validators import UniqueValidator
from rest_framework_json_api.relations import ResourceRelatedField
from django.contrib.auth.models import User, Group
from users.models import UserAddress
from common.models import City
from common.serializers import CitySerializer

# Create your serializers here.

class GroupSerializer(HyperlinkedModelSerializer):
  class Meta:
    model = Group
    fields = ['url', 'name']

class UserSerializer(HyperlinkedModelSerializer):
  groups = ResourceRelatedField (
    queryset = Group.objects,
    many = True,
    required = False
  )
  email = serializers.EmailField (
    required = True,
    validators = [
      UniqueValidator(queryset=User.objects.all())
    ]
  )
  included_serializers = {
    'groups': GroupSerializer
  }

  class Meta:
    model = User
    fields = [
      'url','username', 'email', 'last_login',
      'first_name', 'last_name', 'password',
      'is_superuser', 'groups', 'date_joined',
      'is_active', 'is_staff'
    ]
    extra_kwargs = {
      'password': {
        'write_only': True,
        'required': False
      },
      'is_superuser': {
        'read_only': True
      },
      'is_staff': {
        'read_only': True
      },
      'is_active': {
        'read_only': True
      },
      'last_login': {
        'read_only': True
      },
      'date_joined': {
        'read_only': True
      }
    }

  def create(self, validated_data):
    user = User()
    for i in validated_data:
      setattr(user, i, validated_data[i])
    user.set_password(validated_data['password'])
    user.save()
    return user

  def update(self, instance, validated_data):
    for i in validated_data:
      setattr(instance, i, validated_data[i])
    if 'password' in validated_data:
      instance.set_password(validated_data['password'])
    instance.save()
    return instance


class UserAddressSerializer(HyperlinkedModelSerializer):
    user = ResourceRelatedField (
      queryset = User.objects,
      required = False
    )
    city = ResourceRelatedField (
      queryset = City.objects,
      required = False
    )
    included_serializers = {
      'city': CitySerializer,
      'user': UserSerializer
    }

    class Meta:
      model = UserAddress
      fields = '__all__'
      extra_kwargs = {
        'user': {
          'read_only': True
        },
        'created': {
          'read_only': True
        },
        'modified': {
          'read_only': True
        }
      }