import os

environment = None
db_name = 'iguzman'
db_user = 'iguzman'
db_password = 'iguzman'

if 'env' in os.environ:
  environment = os.environ['env']

if 'db_name' in os.environ:
  db_name = os.environ['db_name']
if 'db_user' in os.environ:
  db_user = os.environ['db_user']
if 'db_password' in os.environ:
  db_password = os.environ['db_password']

class Common:
  SITE_HEADER = "iGuzman"
  INDEX_TITLE = "CMS"
  SITE_TITLE = "CMS"

  EMAIL_HOST = "smtp.gmail.com"
  EMAIL_USE_TLS = True
  EMAIL_PORT = 587


class LOCAL(Common):
  DEBUG = True
  ALLOWED_HOSTS = ['*']
  EMAIL_HOST_USER = "christopher.guzman.monsalvo@gmail.com"
  EMAIL_HOST_PASSWORD = 'password'
  DATABASES = {
    'default': {
      'ENGINE': 'django.contrib.gis.db.backends.postgis',
      'NAME': db_name,
      'USER': db_user,
      'PASSWORD': db_password,
      'HOST': '127.0.0.1',
      'PORT': '5432'
    },
  }
  JWT_EXPIRATION_DAYS = 720
  MAP_WIDGETS = {
    "GooglePointFieldWidget": (
      ("zoom", 12),
      ("mapCenterLocationName", "mexico city"),
      ("GooglePlaceAutocompleteOptions",{}),
      ("markerFitZoom", 12),
    ),
    "GOOGLE_MAP_API_KEY": "AIzaSyDXYSvqhFzPFT_M3rgEMl5_h0bbZZ7090g"
  }


class QA(Common):
  DEBUG = True
  ALLOWED_HOSTS = ['*']
  EMAIL_HOST_USER = "christopher.guzman.monsalvo@gmail.com"
  EMAIL_HOST_PASSWORD = 'password'
  DATABASES = {
    'default': {
      'ENGINE': 'django.contrib.gis.db.backends.postgis',
      'NAME': db_name,
      'USER': db_user,
      'PASSWORD': db_password,
      'HOST': '127.0.0.1',
      'PORT': '5432'
    },
  }
  JWT_EXPIRATION_DAYS = 720
  MAP_WIDGETS = {
    "GooglePointFieldWidget": (
      ("zoom", 12),
      ("mapCenterLocationName", "mexico city"),
      ("GooglePlaceAutocompleteOptions",{}),
      ("markerFitZoom", 12),
    ),
    "GOOGLE_MAP_API_KEY": "AIzaSyDXYSvqhFzPFT_M3rgEMl5_h0bbZZ7090g"
  }


class STAGING(Common):
    DEBUG = True
    ALLOWED_HOSTS = ['*']
    EMAIL_HOST_USER = "christopher.guzman.monsalvo@gmail.com"
    EMAIL_HOST_PASSWORD = 'password'
    DATABASES = {
      'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': db_name,
        'USER': db_user,
        'PASSWORD': db_password,
        'HOST': '127.0.0.1',
        'PORT': '5432'
      },
    }
    JWT_EXPIRATION_DAYS = 7
    MAP_WIDGETS = {
      "GooglePointFieldWidget": (
        ("zoom", 12),
        ("mapCenterLocationName", "mexico city"),
        ("GooglePlaceAutocompleteOptions",{}),
        ("markerFitZoom", 12),
      ),
      "GOOGLE_MAP_API_KEY": "AIzaSyDXYSvqhFzPFT_M3rgEMl5_h0bbZZ7090g"
    }

class MASTER(Common):
    DEBUG = True
    ALLOWED_HOSTS = ['*']
    EMAIL_HOST_USER = "christopher.guzman.monsalvo@gmail.com"
    EMAIL_HOST_PASSWORD = 'password'
    DATABASES = {
      'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': db_name,
        'USER': db_user,
        'PASSWORD': db_password,
        'HOST': '127.0.0.1',
        'PORT': '5432'
      },
    }
    JWT_EXPIRATION_DAYS = 7
    MAP_WIDGETS = {
      "GooglePointFieldWidget": (
        ("zoom", 12),
        ("mapCenterLocationName", "mexico city"),
        ("GooglePlaceAutocompleteOptions",{}),
        ("markerFitZoom", 12),
      ),
      "GOOGLE_MAP_API_KEY": "AIzaSyDXYSvqhFzPFT_M3rgEMl5_h0bbZZ7090g"
    }

if environment == 'qa':
  env = QA
elif environment == 'staging':
  env = STAGING
elif environment == 'master':
  env = MASTER
else:
  env = LOCAL
