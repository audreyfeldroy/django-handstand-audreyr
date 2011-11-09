from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Locally, it's easiest to use your own user account to createdb/dropdb
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'handstand',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}


# For django-social-auth
TWITTER_CONSUMER_KEY         = 'DEFINE-ME-HERE--DO-NOT-CHECK-IN-PUBLICLY'
TWITTER_CONSUMER_SECRET      = 'DEFINE-ME-HERE--DO-NOT-CHECK-IN-PUBLICLY'
FACEBOOK_APP_ID              = 'DEFINE-ME-HERE--DO-NOT-CHECK-IN-PUBLICLY'
FACEBOOK_API_SECRET          = 'DEFINE-ME-HERE--DO-NOT-CHECK-IN-PUBLICLY'


# For django-debug-toolbar
INSTALLED_APPS += ('debug_toolbar',)
INTERNAL_IPS = ('127.0.0.1', 'YOUR-IP-ADDRESS-HERE')

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}
