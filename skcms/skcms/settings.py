"""
Django settings for skcms project.

Generated by 'django-admin startproject' using Django 1.11.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xr-2sr07=)ereqr&=ny)sk5&6ovo4w5^y4p$l!3d7iz_ff3f3_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'address_book',
    'group',
    'user_profile',
    'notifications',
    # 'permission',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'middleware.LoginRequiredMiddleware',
]

ROOT_URLCONF = 'skcms.urls'

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
                'address_book.my_context_processor.my_cp',
            ],
            # 'builtins': [
            #     'permission.templatetags.permissionif'
            # ],
        },
    },
]

WSGI_APPLICATION = 'skcms.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Warsaw'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static/'),
]

MEDIA_URL = '/media/'

AUTH_PROFILE_MODULE = 'user_profile.UserProfile'

LOGIN_URL = '/accounts/login/'

# Login required urls exceptions
STRONGHOLD_PUBLIC_URLS = (
    r'/accounts/create_user/',
    r'/accounts/auth/',
)
#
# # permission
# AUTHENTICATION_BACKENDS = (
#     'django.contrib.auth.backends.ModelBackend', # default
#     'permission.backends.PermissionBackend',
# )
#
# # # PERMISSION_CHECK_AUTHENTICATION_BACKENDS
# # PERMISSION_CHECK_AUTHENTICATION_BACKENDS = []
# # PERMISSION_REPLACE_BUILTIN_IF = []
# # PERMISSION_CHECK_TEMPLATES_OPTIONS_BUILTINS = []
# # TEMPLATES = ['persons.html',]
#
# # permission collaborators
# PERMISSION_DEFAULT_COLLABORATORS_PERMISSION_LOGIC_FIELD_NAME = 'user'
# PERMISSION_DEFAULT_COLLABORATORS_PERMISSION_LOGIC_ANY_PERMISSION = True
# PERMISSION_DEFAULT_COLLABORATORS_PERMISSION_LOGIC_CHANGE_PERMISSION = True
# PERMISSION_DEFAULT_COLLABORATORS_PERMISSION_LOGIC_DELETE_PERMISSION = False
#
# # permission user
# PERMISSION_DEFAULT_APL_FIELD_NAME = 'user'
# PERMISSION_DEFAULT_APL_ANY_PERMISSION = True
# PERMISSION_DEFAULT_APL_CHANGE_PERMISSION = True
# PERMISSION_DEFAULT_APL_DELETE_PERMISSION = False
