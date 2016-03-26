from .common import *

DEBUG = False
ALLOWED_HOSTS = ['*']

STATIC_ROOT = os.path.join(BASE_DIR, "..", "staticfiles")
MEDIA_ROOT = os.path.join(BASE_DIR, "..", "media")

# Django 내 암호화 시에 Salt 값으로 씁니다.
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', SECRET_KEY)

DATABASES = {
    'default': {
    #'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'ubuntu',
    'USER': 'ubuntu',
    'PASSWORD': 'withaskdjango!',
    'HOST': '127.0.0.1',
    },
}