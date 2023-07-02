"""
Django settings for acordãos project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from pymongo import MongoClient
import os
import datetime
import environ
# Initialise environment variables
env = environ.Env()
environ.Env.read_env()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['0.0.0.0','localhost','127.0.0.1', 'api-server','*','172.26.113.96', 'eivarin.xyz']


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    
    'rest_framework',
    'rest_framework_api_key',
    "rest_framework_swagger",
    'drf_yasg',
    'corsheaders',
    'drf_spectacular',
    
    'accounts',
    'records',
    'favorites'
]
AUTH_USER_MODEL='accounts.Account'

AUTHENTICATION_BACKENDS = (
    'accounts.authentication.APIKeyAuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',
)

SITE_ID = 1
ACCOUNT_EMAIL_VERIFICATION = 'none'

REST_FRAMEWORK = {
   'DEFAULT_AUTHENTICATION_CLASSES': (
        'accounts.authentication.APIKeyAuthenticationBackend',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
   ),
   
   'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema'
}


# JWT settings
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(days=31),
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=365),
}


SPECTACULAR_SETTINGS = {
    'TITLE': 'Acordb Server'
}

CORS_ORIGIN_ALLOW_ALL = True


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = "acordãos.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS=False
WSGI_APPLICATION = "acordãos.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('POSTGRESQL_NAME'),
        'USER': env('POSTGRESQL_USER'),
        'PASSWORD': env('POSTGRESQL_PASSWORD'),
        'HOST': env('POSTGRESQL_HOST'),
        'PORT': env('POSTGRESQL_PORT')
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = env("TIME_ZONE")

USE_I18N = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")

STATICFILES_DIRS = [
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"




# Facebook API settings
SOCIALACCOUNTS = {
    'facebook': {
        'client_id': '172096125699052',
        'secret': '4129a410c152648a9775efa402f9eb98',
    },
}
GOOGLE_CLIENT_ID=env('GOOGLE_CLIENT_ID')
GOOGLE_SECRET=env('GOOGLE_SECRET')
MONGO_DB_CONNECTION_STRING=env('MONGO_DB_CONNECTION_STRING')
MONGO_DB_NAME=env('MONGO_DB_NAME')

MONGO_DB = MongoClient(MONGO_DB_CONNECTION_STRING,socketTimeoutMS=500000)[MONGO_DB_NAME]
MONGO_DB['records'].create_index([('id_acordao', 1), ('record_added_at', -1)])
MONGO_DB['records'].create_index([('record_added_at', -1)])
DATA_UPLOAD_MAX_NUMBER_FIELDS=1000000