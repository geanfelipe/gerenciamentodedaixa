"""
Django settings for pizzaria project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
import dj_database_url


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ac7go^b7q4(u6_dj$)$wmsb^cczy-w=x#ucq$c#(&b(swz6l0-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

TEMPLATE_PATH = os.path.join(BASE_DIR,'templates')

TEMPLATE_DIRS = [
    TEMPLATE_PATH,
]


ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'caixa',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'pizzaria.urls'

WSGI_APPLICATION = 'pizzaria.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

if not os.environ.has_key('DATABASE_URL'):
    os.environ['DATABASE_URL'] = 'postgres://postgres:admin@localhost/pizzaria'
DATABASES = {'default': dj_database_url.config(default=os.environ['DATABASE_URL'])}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Fortaleza'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = "/media/"

STATIC_PATH = os.path.join(BASE_DIR,'static')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_URL = '/static/' #ex: http://127.0.0.1:8000/static/ 

STATICFILES_DIRS=(
    STATIC_PATH,

)