"""
Django settings for fdu project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

gettext_noop = lambda s: s

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0sisw260d%dwxc1nb6f$9why^6uyp@_3nz*cu-1-*^+%i*^(61'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)

ALLOWED_HOSTS = []

ADMINS = (
    'msaelices@gmail.com',
    'berto.suero@gmail.com',
)

# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'modeltranslation',
    'inplaceeditform',
    'suit',  # has to be before django admin
    'django.contrib.admin',
    'django_summernote',
    'rosetta',
    # FDU apps
    'landing',
    'chunks',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

ROOT_URLCONF = 'fdu.urls'

WSGI_APPLICATION = 'fdu.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

LANGUAGE_CODE = 'es-es'

LANGUAGES = (
    ('en', gettext_noop('English')),
    ('es', gettext_noop('Spanish')),
)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

CHIRIPONES_REGISTRATION_DATE = (10, 1)

# django-suit

SUIT_CONFIG = {
    'ADMIN_NAME': 'Frisbillanas',
    # menu
    'MENU_ICONS': {
        'sites': 'icon-leaf',
        'auth': 'icon-lock',
        'home': 'fa fa-home'
    },
    'MENU_OPEN_FIRST_CHILD': True,  # Default True
    'MENU': (
        '-',
        {'app': 'chunks', 'label': 'Fragmentos de texto', 'icon': 'fa fa-comments-o',},

    ),

    # misc
    'LIST_PER_PAGE': 20
}

try:
    # Try import local settings
    from settings_local import *
except ImportError:
    pass
