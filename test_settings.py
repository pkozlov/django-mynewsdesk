# -*- coding: utf-8 -*-

SECRET_KEY = 'test'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

INSTALLED_APPS = (
    'mynewsdesk',
)

MYNEWSDESK_KEY = 'unique_key'

STATIC_ROOT = '/tmp/'  # Dummy
