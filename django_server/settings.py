"""
Django settings for django_server project.

Generated by 'django-admin startproject' using Django 2.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import sys
import django_server

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#)3@frpj&sdx6(si+ul=3cnte7nec@^j_0pihj4!d9362vw!r@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', '') == '1'

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'app.apps.DjangoAppConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_swagger',
    'django_prometheus',
]

REST_FRAMEWORK = {}


MIDDLEWARE = [
    'django_prometheus.middleware.PrometheusBeforeMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_prometheus.middleware.PrometheusAfterMiddleware',
]

ROOT_URLCONF = 'django_server.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'app', 'templates')],
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

WSGI_APPLICATION = 'django_server.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

USE_DB = os.environ.get("USE_DB", "0") == "1"

if USE_DB:
    DATABASES = {
        'default': {
            'ENGINE': 'django_prometheus.db.backends.mysql',
            'NAME': os.environ.get('MYSQL_NAME', 'FILL'),
            'USER': os.environ.get('MYSQL_USER', 'FILL'),
            'PASSWORD': os.environ.get('MYSQL_PASSWORD', 'FILL'),
            'HOST': os.environ.get('MYSQL_HOST', 'FILL'),
            'PORT': 3306,
            'OPTIONS': {'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"},
        },
        'slave': {
            'ENGINE': 'django_prometheus.db.backends.mysql',
            'NAME': os.environ.get('MYSQL_SLAVE_NAME', os.environ.get('MYSQL_NAME')),
            'USER': os.environ.get('MYSQL_SLAVE_USER', os.environ.get('MYSQL_USER')),
            'PASSWORD': os.environ.get('MYSQL_SLAVE_PASSWORD', os.environ.get('MYSQL_PASSWORD')),
            'HOST': os.environ.get('MYSQL_SLAVE_HOST', os.environ.get('MYSQL_HOST')),
            'PORT': 3306,
            'OPTIONS': {'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"},
        }
    }
else:
    DATABASES = {}

if os.environ.get('LOG_FORMAT', '') == 'json':
    log_level = 'DEBUG' if DEBUG else 'INFO'
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'logstash': {
                'class': 'django_server.log.LogstashLowerLevelFormatterV1'
            },
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'stream': sys.stdout,
                'level': log_level,
                'formatter': 'logstash',
            },
        },
        'loggers': {
            'django': {
                'level': log_level,
                'handlers': ['console'],
                'propagate': False,
            },
            'django_server': {
                'level': log_level,
                'handlers': ['console'],
                'propagate': False,
            },
            'gunicorn': {
                'level': log_level,
                'handlers': ['console'],
                'propagate': False,
            },
        },
        'root': {
            'handlers': ['console'],
            'level': 'INFO',
        }
    }
else:
    LOGGING = {}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

# LANGUAGE_CODE = 'cs-cz'
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Prague'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'static'))


# Testing config overloading
if 'test' in sys.argv or 'test_coverage' in sys.argv or 'TEST' in os.environ:
    DATABASES = {'default': {'ENGINE': 'django_prometheus.db.backends.sqlite3', 'NAME': 'test.db'}}
