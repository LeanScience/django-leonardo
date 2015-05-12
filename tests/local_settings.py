from __future__ import absolute_import, unicode_literals

import os

SITE_ID = 1

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'memory:',
        'TEST_NAME': 'test_db:',
    }
}

MEDIA_URL = '/media/'
STATIC_URL = '/static/'
BASEDIR = os.path.dirname(__file__)
MEDIA_ROOT = os.path.join(BASEDIR, 'media/')
STATIC_ROOT = os.path.join(BASEDIR, 'static/')
SECRET_KEY = 'supersikret'
USE_TZ = True

ROOT_URLCONF = 'testapp.urls'
LANGUAGES = (('en', 'English'), ('cs', 'Czech'))

LEONARDO_MODULE_AUTO_INCLUDE = False

APPS = [
    'web',
    'testapp',
    'media',
]

MIGRATION_MODULES = {
    'web': 'notmigrations',
    'filer': 'notmigrations',
}
