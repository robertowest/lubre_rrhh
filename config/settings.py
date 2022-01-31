"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 2.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'cn1-^op%h5-tz-j!apcs_3w5rim#pa!v+5%@#bc_1lin%)y3+n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.messages',
    'django.contrib.sessions',
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

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # accederá al directorio templates del proyecto
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
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {},
    'sqlite': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'mysql': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'lubre_dev',  # 'lubre_dev': desarrollo 'lubresl': produccion
        'USER': 'roberto',
        'PASSWORD': 'roberto',
        'HOST': '192.168.1.2',
        'PORT': '3306',
    },
    'firebird': {
        'ENGINE': 'django.db.backends.firebird',
        'NAME': 'P:\PRUEBA\DATOS\GESTION.FDB',
        'USER': 'SYSDBA',
        'PASSWORD': 'masterkey',
        'HOST': '192.168.1.254',
        'PORT': '3050',
        'OPTIONS': {'charset': 'ISO8859_1'}
    },
}

DATABASE_ROUTERS = ['config.routers.MySQLRouter',
                    'config.routers.FirebirdRouter']

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]
AUTH_PASSWORD_VALIDATORS = []

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Argentina/Tucuman'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

# -----------------------------------------------------------------------------
ALLOWED_HOSTS = ['*']

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    # os.path.join(BASE_DIR, 'apps/person/statics'),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# python manage.py collectstatic
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')

# configuración debug-toolbar
if DEBUG:
    INSTALLED_APPS += [
        'debug_toolbar',
    ]

    MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]

    INTERNAL_IPS = ['localhost', '127.0.0.1', '172.19.0.1']  # gateway del docker
# fin configuración debug-toolbar

INSTALLED_APPS += [
    # aplicacione de terceros
    'bootstrap_modal_forms',
    'business_calendar',
    'crispy_forms',
    'datetimepicker',
    'django_extensions',
    'django_filters',
    'mathfilters',
    'widget_tweaks',
    # mis aplicaciones
    'apps.blog',
    'apps.homepage',
    'apps.clientes',
    'apps.juridico',
    'apps.rrhh',
    'apps.usuarios',
]

# redirecciona a home al realizar un login exitoso
LOGIN_URL = '/usuarios/inicio/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_URL = '/usuarios/salir/'
LOGOUT_REDIRECT_URL = '/'

# para que funcione el proceso de registro de usuarios
# esto evitará que se envíe un email e imprimirá el resultado por la consola
EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = os.path.join(BASE_DIR, "static/sent_emails")
