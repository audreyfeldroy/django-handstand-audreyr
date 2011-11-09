from .base import *

# For production, create a separate user for your PostgreSQL db
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'handstand',
        'USER': 'handstand',
        'PASSWORD': 'DEFINE-ME-HERE--DO-NOT-CHECK-IN-PUBLICLY',
        'HOST': '',
        'PORT': '',
    }
}

# Set up outgoing email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_PASSWORD = ''
EMAIL_HOST_USER = 'someone@yoursite.com'
EMAIL_PORT = 587
EMAIL_SUBJECT_PREFIX = '[Your Site]'
EMAIL_USE_TLS = True
SERVER_EMAIL = 'someone@yoursite.com'
