"""
Django settings for MaraudersMap project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

DEBUG=True

#DEBUG_TOOLBAR_PATCH_SETTINGS = False



BASE_DIR = os.path.dirname(os.path.dirname(__file__))

STATIC_ROOT = '/sid-static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',

)
SERIALIZATION_MODULES = {
    'geojson': 'djgeojson.serializers'
}


REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),
    'PAGINATE_BY': 10
}
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_URL = '/sid-static/'

STATIC_PATH = os.path.join(BASE_DIR, 'sid-static')

STATICFILES_DIRS = (
    STATIC_PATH,
)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5g7zxeai=ecncq5rmxm2+nl$a!xqmhwihmtmdauz-u3(fu_9p1'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') # Absolute path to the media directory



TEMPLATE_DEBUG = True
TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')
TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    TEMPLATE_PATH,
)
ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'grappelli',
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.gis',
    'olwidget',
    'south',
    #'semantic_mapping',
    'marmap_users',
    'semantic_mapping',
    'app',

    #third party other than grappelli and south
    'rest_framework',
    'rest_framework_swagger',
    'django_extensions',
    'model_utils',
    'djgeojson',
    'django_filters',
    'leaflet',

    #Testing and dev.:
    'viewtools',
 #   'debug_toolbar',
    'model_mommy',

)

# Your setting will look like:
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'apptemplates.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
   # 'debug_toolbar.middleware.DebugToolbarMiddleware',

)

ROOT_URLCONF = 'MaraudersMap.urls'

WSGI_APPLICATION = 'MaraudersMap.wsgi.application'



# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'maraudersmap',
        'USER': 'harry',
        'PASSWORD': 'harry',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

#Naive Timezone setting is allowed only w/ PostgreSQL!!!!!!
USE_TZ = False

GRAPPELLI_ADMIN_TITLE = 'Marauder\'s Map Admin'






