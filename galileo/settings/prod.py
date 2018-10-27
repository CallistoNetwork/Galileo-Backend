from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS += [
    'gunicorn'
]

# STATIC_URL = '/clo-audit/static/'

# SECURE_DOMAIN = 'https://callisto.network/'
