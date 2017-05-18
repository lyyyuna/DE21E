"""
Django settings for notes project.

Generated by 'django-admin startproject' using Django 1.11.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9ykizdh(^oql#!l)haj)f8ruug@wdfea!0qjt%pz@9ui!$xsic'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'draceditor',
    'flower',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'notes.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'notes.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

# Global draceditor settings
# Input: string boolean, `true/false`
DRACEDITOR_ENABLE_CONFIGS = {
    'imgur': 'false',     # to enable/disable imgur/custom uploader.
    'mention': 'false',  # to enable/disable mention
    'jquery': 'true',    # to include/revoke jquery (require for admin default django)
}

# Imgur API Keys
DRACEDITOR_IMGUR_CLIENT_ID = 'your-client-id'
DRACEDITOR_IMGUR_API_KEY   = 'your-api-key'

# Safe Mode
DRACEDITOR_MARKDOWN_SAFE_MODE = True # default

# Markdownify
DRACEDITOR_MARKDOWNIFY_FUNCTION = 'draceditor.utils.markdownify' # default
DRACEDITOR_MARKDOWNIFY_URL = '/draceditor/markdownify/' # default

# Markdown extensions (default)
DRACEDITOR_MARKDOWN_EXTENSIONS = [
    'markdown.extensions.extra',
    'markdown.extensions.nl2br',
    'markdown.extensions.smarty',
    'markdown.extensions.fenced_code',

    # Custom markdown extensions.
    'draceditor.extensions.urlize',
    'draceditor.extensions.del_ins', # ~~strikethrough~~ and ++underscores++
]

# Markdown Extensions Configs
DRACEDITOR_MARKDOWN_EXTENSION_CONFIGS = {}

# Markdown urls
DRACEDITOR_UPLOAD_URL = '/draceditor/uploader/' # default
DRACEDITOR_SEARCH_USERS_URL = '/draceditor/search-user/' # default

# Markdown Extensions
DRACEDITOR_MARKDOWN_BASE_EMOJI_URL = 'https://assets-cdn.github.com/images/icons/emoji/' # default
DRACEDITOR_MARKDOWN_BASE_MENTION_URL = 'https://forum.dracos-linux.org/profile/' # default (change this)