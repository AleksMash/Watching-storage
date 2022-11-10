import os
from environs import Env

env=Env()
env.read_env()

DATABASES = {
    'default': {
        'ENGINE': env.str('ENGINE'),
        'HOST': env.str('HOST'),
        'PORT': env.str('PORT'),
        'NAME': env.str('NAME'),
        'USER': env.str('USER'),
        'PASSWORD': env.str('PASSWORD'),
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': os.getenv('ENGINE'),
#         'HOST': os.getenv('HOST'),
#         'PORT': os.getenv('PORT'),
#         'NAME': os.getenv('NAME'),
#         'USER': os.getenv('USER'),
#         'PASSWORD': os.getenv('PASSWORD'),
#     }
# }


INSTALLED_APPS = ['datacenter']

SECRET_KEY = 'REPLACE_ME'

DEBUG = env.bool('DEBUG')

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = ['*']



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'