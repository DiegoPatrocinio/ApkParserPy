import os
import getpass
import djcelery
djcelery.setup_loader()


#DEBUG = os.getenv('DEBUG', 'NO').lower() in ('on', 'true', 'y', 'yes')

DEBUG = True

PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

FILESIZELIMIT = 1048576 * 5
MANAGERS = ADMINS
ADMIN_PHONE = ''
ADMIN_EMAIL = 'admin@voidsolution.com'
GEOPOSITION_GOOGLE_MAPS_API_KEY = 'AIzaSyCERaaHlAVJAlm4d10mNWfzhsvlYNnVAJ0'

GEOPOSITION_MAP_OPTIONS = {
    'minZoom': 3,
    'maxZoom': 15,
}

GEOPOSITION_MARKER_OPTIONS = {
    'cursor': 'move'
}

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ.get('DB_NAME', 'apkparse'),
            'USER': os.environ.get('DB_USER', 'apkparse'),
            'PASSWORD': os.environ.get('DB_PASS', 'apkparse'),
            'HOST': os.environ.get('DB_SERVICE', 'apkparse'),
            'PORT': os.environ.get('DB_PORT', 3306)
        }
    }

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['*']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Asia/Jakarta'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = False

MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(PROJECT_PATH, 'static')
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'

# CAPTCHA SETTINGS
CAPTCHA_FONT_PATH = os.path.join(PROJECT_PATH, 'courier.ttf')
CAPTCHA_FONT_SIZE = 34

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    #'compressor.finders.CompressorFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = os.environ.get('SECRET_KEY', '#rj!&#1r333u81l!lm8w1$u_989(e1gd88i!51irap(b_omv8k')

MIDDLEWARE_CLASSES = (
    'backoffice.middleware.DefaultMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'responsive.middleware.DeviceInfoMiddleware',
    'django_user_agents.middleware.UserAgentMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

LOGIN_URL = '/login/'
ROOT_URLCONF = 'urls'


DEFAULT_BREAKPOINTS = {
    'phone': 480,
    'tablet': 767,
    'desktop': None,
}


# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'backoffice.wsgi.application'


# compression setup
#COMPRESS_ENABLED = True
#COMPRESS_CSS_FILTERS = ['compressor.filters.css_default.CssAbsoluteFilter', 'compressor.filters.cssmin.CSSMinFilter']
#COMPRESS_URL = MEDIA_URL
#COMPRESS_ROOT = MEDIA_ROOT
#COMPRESS_PARSER = 'compressor.parser.LxmlParser'

DJANGO_WYSIWYG_FLAVOR = "tinymce_advanced"

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}
USER_AGENTS_CACHE = 'default'


INSTALLED_APPS = (
    'djcelery',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    #'material',
    #'material.frontend',
    #'material.admin',
    'django.contrib.admin',
    'django_wysiwyg',
    'tinymce',
    #'compressor',
    'django_user_agents',
    #'paypal.standard.ipn',
    'rest_framework',
    'django_filters',
    #'taggit_serializer',
    #'sorl.thumbnail',
    #'sorl_thumbnail_serializer',

    'backoffice',
    'api',
    'geoposition',

    #'captcha',
    #'djorm_pgfulltext',
    'responsive',
    'easy_thumbnails',
    #'import_export',
    #'service',
    #'taggit',
    #'django_countries',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    #'allauth',
    #'allauth.account',
    #'allauth.socialaccount',
    # ... include the providers you want to enable:
    #'allauth.socialaccount.providers.facebook',
    #'allauth.socialaccount.providers.google',
    #'allauth.socialaccount.providers.twitter',
)

THUMBNAIL_ALIASES = {
    '': {
        'foto': {'size': (100, 100), 'crop': True},
    },
}

PAYPAL_TEST = True
PAYPAL_RECEIVER_EMAIL = ''

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

ACCOUNT_EMAIL_REQUIRED      = True
EMAIL_CONFIRMATION_SIGNUP   = False
ACCOUNT_EMAIL_VERIFICATION  = None

# Specify the context processors as follows:
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PROJECT_PATH, 'templates')],
        'OPTIONS': {
            'loaders':[
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            'debug':DEBUG,
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.core.context_processors.i18n',
                'django.core.context_processors.request',
                'django.core.context_processors.media',
                'django.core.context_processors.static',
                'responsive.context_processors.device_info',

                # `allauth` needs this from django
                'django.template.context_processors.request',
            ],
        },
    },
]

REST_FRAMEWORK = {
    # 'DEFAULT_RENDERER_CLASSES': (
    #     'rest_framework.renderers.JSONRenderer',
    # ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100
}
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(PROJECT_PATH, 'log/django.log'),
            'maxBytes': 1024*1024*5, # 5 MB
            'backupCount': 5,
            'formatter':'standard',
        },
        'request_handler': {
                'level':'DEBUG',
                'class':'logging.handlers.RotatingFileHandler',
                'filename': os.path.join(PROJECT_PATH, 'log/django.log'),
                'maxBytes': 1024*1024*5, # 5 MB
                'backupCount': 5,
                'formatter':'standard',
        },
    },
    'loggers': {

        '': {
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': True
        },
        'django.request': {
            'handlers': ['request_handler'],
            'level': 'DEBUG',
            'propagate': False
        },
    }
}
