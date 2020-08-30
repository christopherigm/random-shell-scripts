"""iguzman_db URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from rest_framework import routers

from rest_framework_simplejwt.views import (
  TokenObtainPairView,
  TokenRefreshView,
  TokenVerifyView,
)

from users.views import (
  UserViewSet,
  GroupViewSet,
  UserAddressViewSet
)
from common.views import (
  CountryViewSet,
  StateViewSet,
  CityViewSet,
  System
)
from pages.views import (
  ModuleViewSet,
  PageAddressViewSet,
  PageViewSet,
  SectionViewSet
)
from nav_bar.views import NavBarViewSet
from slides.views import (
  SlidePicturesViewSet,
  SlideViewSet
)
from banner.views import BannerViewSet
from info_grid.views import (
  InfoGridViewSet,
  InfoGridItemViewSet
)
from video_banner.views import VideoBannerViewSet
from photo_mosaic.views import (
  PhotoMosaicItemViewSet,
  PhotoMosaicViewSet
)

router = routers.DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'user-address', UserAddressViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'countries', CountryViewSet)
router.register(r'states', StateViewSet)
router.register(r'cities', CityViewSet)
router.register(r'page-address', PageAddressViewSet)
router.register(r'pages', PageViewSet)
router.register(r'sections', SectionViewSet)
router.register(r'modules', ModuleViewSet)
router.register(r'nav_bars', NavBarViewSet)
router.register(r'banners', BannerViewSet)
router.register(r'info-grids', InfoGridViewSet)
router.register(r'info-grid-items', InfoGridItemViewSet)
router.register(r'slides', SlideViewSet)
router.register(r'slide-items', SlidePicturesViewSet)
router.register(r'video-banners', VideoBannerViewSet)
router.register(r'photo-mosaics', PhotoMosaicViewSet)
router.register(r'photo-mosaic-items', PhotoMosaicItemViewSet)

urlpatterns = [
  path('admin/', admin.site.urls),
]

urlpatterns = [
  url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
  path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
  path('admin/', admin.site.urls),
  url(r'^v1/', include(router.urls)),
  path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
  url(r'^api/token/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  url(r'^api/token/refresh/$', TokenRefreshView.as_view(), name='token_refresh'),
  url(r'^api/token/verify/$', TokenVerifyView.as_view(), name='token_verify'),
  url(r'^tinymce/', include('tinymce.urls')),
  path('system/info', System.info)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
