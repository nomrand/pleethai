import dj_database_url
import django.core.management.utils
import django_heroku
"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 2.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# *** SETTING FOR LOCAL DEVELOPMENT ENVIRONMENT ***
SECRET_KEY = django.core.management.utils.get_random_secret_key()

# SECURITY WARNING: don't run with debug turned on in production!
# *** SETTING FOR LOCAL DEVELOPMENT ENVIRONMENT ***
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
    'import_export',
    'crispy_forms',
    'pleethai',
    'taggit',
    'gmailapi_backend'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'th'

LANGUAGES = [('ja', 'Japanese'), ('th', 'Thai')]

TIME_ZONE = 'Asia/Bangkok'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Locale
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

# Parse database configuration from $DATABASE_URL
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# crispy
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Static asset configuration
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Mail send
# *** SETTING FOR LOCAL DEVELOPMENT ENVIRONMENT ***
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'request_mails')

REQUEST_MAIL_SEND_INFO = {
    'subject': 'GaifaaYeepun Request Mail',
    'templete_path': 'mails/request.txt',
    'from_email': 'from@test.com',
    'recipient_list': [
        'to@test.com',
    ],
}

# About Page URL
# *** SETTING FOR LOCAL DEVELOPMENT ENVIRONMENT ***
ABOUT_URL_MAP = {
    'ja' : '',
    'en' : '',
    'th' : '',
}

# *** SETTING FOR PRODUCTION ENVIRONMENT ***
# load "production_settings.py" & overwrite development settings
# (no exist = development setting)
try:
    from .production_settings import *
except ImportError:
    pass

# Heroku Setting
SECRET_KEY = 'yftgrj&zt8=06mv7(hhum(fjceo2f$3$*xlo7m2gsq&fh92zrf'
# Activate Django-Heroku.
django_heroku.settings(locals())
