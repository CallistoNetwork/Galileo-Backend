from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS += [
    'django_extensions'
]

CORS_ORIGIN_WHITELIST = (
    '*',
    'localhost:3001',
    '192.168.64.13:3001',
    '127.0.0.1:3001'
)

# SECURE_DOMAIN = 'https://stg.callisto.network/'
