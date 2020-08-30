from django.contrib import admin
from django.contrib.gis.db.models import PointField
from mapwidgets.widgets import GooglePointFieldWidget
from users.models import (
  UserAddress,
  UserProfile
)

# Register your models here.

class UserAddressAdmin(admin.ModelAdmin):
  list_display = [
    'alias',
    'city',
    'enabled'
  ]
  search_fields = ('alias',)
  list_filter = ('enabled','city')
  formfield_overrides = {
    PointField: {
      'widget': GooglePointFieldWidget
    }
  }
admin.site.register(UserAddress, UserAddressAdmin)

class UserProfileAdmin(admin.ModelAdmin):
  list_display = [
    'user',
    'language',
    'currency'
  ]
  list_filter = ('language','currency')
admin.site.register(UserProfile, UserProfileAdmin)
