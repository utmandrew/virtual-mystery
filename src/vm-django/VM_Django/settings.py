"""
Django settings for VM_Django project.

Generated by 'django-admin startproject' using Django 2.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4^7f5krp_bjs(i67^g*(-nxd)djak2yga7*khl8g85p74jluvq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# Custom user model settings
# refer to https://docs.djangoproject.com/en/2.0/topics/auth/customizing/
AUTH_USER_MODEL = 'system.User'


# for logging, see src/vm-django/logs/logs.txt for usage
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'defaultFormatter': {
            'format': '%(asctime)s [%(levelname)s] - %(message)s',
            'datefmt': '%d/%m/%Y %H:%M:%S',
        },
    },
    'handlers': {
        'activityHandler': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'defaultFormatter',
            'filename': os.path.join(BASE_DIR, '../vm-django/logs/activity.log'),
        },
        'debugHandler': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'defaultFormatter',
            'filename': os.path.join(BASE_DIR, '../vm-django/logs/debug.log'),
        },
    },
    'loggers': {
        'activity': {
            'level': 'INFO',
            'handlers': ['activityHandler'],
        },
        'debug': {
            'level': 'DEBUG',
            'handlers': ['debugHandler'],
        },
    }
}


# Application definition

INSTALLED_APPS = [
    # default apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # new apps
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'comments.apps.CommentsConfig',
    'mystery.apps.MysteryConfig',
    'system.apps.SystemConfig',
    'authentication.apps.AuthenticationConfig',
    'mod_wsgi.server',
]

MIDDLEWARE = [
    # new middleware
    'corsheaders.middleware.CorsMiddleware',
    # default middleware
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'VM_Django.urls'

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

WSGI_APPLICATION = 'VM_Django.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
if 'DOCKER' in os.environ and os.environ.get('DOCKER') == 'True':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ.get('POSTGRES_DB'),
            'USER': os.environ.get('POSTGRES_USER'),
            'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
            'HOST': 'db',
            'PORT': '5432',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'vm_database',
            'USER': 'vm_db_user',
            'PASSWORD': 'vm_password',
            'HOST': 'db',
            'PORT': '5432',
        }
    }

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

# Django Rest Framework
# http://www.django-rest-framework.org

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}

# Django CORS Headers
# https://github.com/ottoyiu/django-cors-headers/

# allow any host to make http requests with the django-rest-framework api.
# comment out the CORS_ORIGIN_WHITELIST if you want to use this feature.
CORS_ORIGIN_ALLOW_ALL = True

# list of authorized hosts allowed to make http requests with the
# django-rest-framework api.
# comment the CORS_ORIGIN_ALLOW_ALL (default to False) if using the whitelist.
# CORS_ORIGIN_WHITELIST = (
#     'localhost:4200',
#     '127.0.0.1:4200',
# )

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

# DateTime for clue release
# https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior

DATETIME_FORMAT = "%d/%m/%Y %H:%M:%S"

if 'DOCKER' in os.environ and os.environ.get('DOCKER') == 'True':
    # mystery start datetime (in datetime format)
    START_DATETIME = os.environ.get('START_DATETIME')

    # time interval in days
    RELEASE_INTERVAL = os.environ.get('RELEASE_INTERVAL')

    # time interval in days (zero for no interval)
    MARK_INTERVAL = os.environ.get('MARK_INTERVAL')

    # mystery end datetime (in datetime format)
    END_DATETIME = os.environ.get('END_DATETIME')

else:
    # mystery start datetime (in datetime format)
    START_DATETIME = "08/12/2019 00:00:00"

    # time interval in days
    RELEASE_INTERVAL = "7"

    # time interval in days (zero for no interval)
    MARK_INTERVAL = "0"

    # mystery end datetime (in datetime format)
    END_DATETIME = "29/12/2019 00:00:00"
