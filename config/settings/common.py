"""
Django settings for nap_site project.
"""
import json

from os import environ
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()


# PATH CONFIGURATION
# ------------------------------------------------------------------------------
DJANGO_ROOT = Path(__file__).resolve().parent.parent
PROJECT_ROOT = DJANGO_ROOT.parent

SITE_NAME = PROJECT_ROOT.name

STATIC_ROOT = PROJECT_ROOT / 'static/'
MEDIA_ROOT = PROJECT_ROOT / 'media/'


# SECRET KEY
# ------------------------------------------------------------------------------
SECRET_KEY = environ['DJANGO_SECRET']


# SECRET KEY
# ------------------------------------------------------------------------------
if 'ALLOWED_HOSTS' in environ:
    ALLOWED_HOSTS = json.loads(environ['ALLOWED_HOSTS'])
else:
    ALLOWED_HOSTS = []


# APPLICATION CONFIGURATION
# ------------------------------------------------------------------------------
INSTALLED_APPS = [
    'basesite.apps.BaseSiteConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        'NAME': environ['DJANGO_DB_NAME'],
        'USER': environ['DJANGO_DB_USER'],
        'PASSWORD': environ['DJANGO_DB_PW']
    }
}


# PASSWORD VALIDATION
# ------------------------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# INTERNATIONALIZATION
# ------------------------------------------------------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Zurich'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# RUNNING CONFIGURATION
# ------------------------------------------------------------------------------
WSGI_APPLICATION = 'config.wsgi.application'
ROOT_URLCONF = 'config.urls'
STATIC_URL = '/static/'
MEDIA_URL = '/media/'


# DEFAULT PRIMARY KEY FIELD TYPE
# ------------------------------------------------------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
