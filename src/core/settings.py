import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
from celery.schedules import crontab

BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = os.environ.get('DEBUG_MODE') == '1'
DEBUG = True

ALLOWED_HOSTS = ['*']
# ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(":")

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',

    'rest_framework',
    'drf_yasg',
    'debug_toolbar',
    'django_filters',
    'main',
    'account',
]

AUTH_USER_MODEL = 'account.user'

INTERNAL_IPS = [
    '127.0.0.1',
]

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 12
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',

    'main.middlwares.URLTrackerMiddleware',
    # 'main.middlwares.SimpleMiddleware',
    # 'main.middlwares.MetrikaMiddleware',
    # 'main.middlwares.LogMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
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

WSGI_APPLICATION = 'core.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(BASE_DIR / 'db.sqlite3'),
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'bread',
#         'USER': 'bread',
#         'PASSWORD': 'bread',
#         'HOST': '10.124.0.3',
#         'PORT': '',
#     }
# }

CACHE = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'memcached:11211'
    }
    # 'default': {
    #     'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
    #     'LOCATION': '192.168.1.3:11211'
    # }
    # "default": {
    #     "BACKEND": "django_redis.cache.RedisCache",
    #     "LOCATION": "redis://127.0.0.1:6379/1",
    # }
}

# CELERY - Configuration Options

# cd src
# celery -A src worker -l info
# CELERY_BROKER_URL = 'amqp://localhost'
# 'amqp://guest:quest@127.0.0.1:5672'
# CELERY_BROKER_URL = '{0}://{1}:{2}@{3}:{4}//'.format(
#     os.environ.get('MQ_DEFAULT_PROTOCOL', 'amqp'),
#     os.environ.get('MQ_DEFAULT_USER', 'guest'),
#     os.environ.get('MQ_DEFAULT_PASS', 'guest'),
#     os.environ.get('MQ_DEFAULT_HOST', '127.0.0.1'),
#     os.environ.get('MQ_DEFAULT_PORT', '5672'),
# )
CELERY_BROKER_URL = '{0}://{1}:{2}/0'.format(
    os.environ.get('MQ_DEFAULT_PROTOCOL', 'redis'),
    os.environ.get('MQ_DEFAULT_HOST', '127.0.0.1'),
    os.environ.get('MQ_DEFAULT_PORT', '127.0.0.1'),
)

CELERY_TIMEZONE = "Europe/Moscow"
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60

# celery -A core beat -l info
# CELERY_BEAT_SCHEDULE = {
#     'smth_slow_async': {
#         'task': 'main.tasks.smth_slow_async',
#         'schedule': crontab(minute='*/1')
#     },
# }

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

# Runserver
STATIC_ROOT = os.path.join(BASE_DIR, '..', 'static_content', 'static')

# Docker
# STATIC_ROOT = os.path.join('/tmp', 'static_content', 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media_content')

# if DEBUG:
#     import socket
#     DEBUG_TOOLBAR_PATCH_SETTINGS = True
#     INTERNAL_IPS += [socket.gethostbyname(socket.gethostname())[:-1] + '1']


# GMAIL
# https://www.google.com/settings/security/lesssecureapps
EMAIL_HOST_USER = 'rmn.storage.1024@gmail.com'
EMAIL_HOST_PASSWORD = 'hi34235464154353453'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


# from django.core.mail import send_mail
#
# send_mail(
#     '222222',
#     '------- asdfasfasf - 2341234',
#     'romanitalian.net@gmail.com',
#     ["romanitalian.net@gmail.com"],
#     fail_silently=False,
# )
#
#
