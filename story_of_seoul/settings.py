"""
Django settings for story_of_seoul project.

Generated by 'django-admin startproject' using Django 3.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import datetime


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'vx9l@qh&fkqoxdbr30#lpg)4uv^rnj%e%-$1%n&kpcm1a#7tsh'

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
    'rest_framework',
    'rest_framework.authtoken',
    'account',
    'board',
    'news',
    'django_filters',
    'corsheaders',
    'analysis',
]


DEFAULT_AUTO_FIELD='django.db.models.AutoField'

REST_FRAMEWORK ={
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
    ],
    'DEFAULT_PAGINATION_CLASS':
    'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE':
    5,

}


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'story_of_seoul.urls'

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

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

WSGI_APPLICATION = 'story_of_seoul.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

#DATABASES = mysettings.DATABASES
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'storyofseoul_db',
        # 'USER': 'root',
        # 'PASSWORD': 'dudqls1659',
        # 'HOST': 'localhost',
        # 'PORT': '3306',
        
        'USER': 'yongcloud',
        'PASSWORD': 'tjdnfdmldldirl',
        'HOST': '13.125.205.105',
        'PORT': '3306',
        
    }
}
'''
SITE_ID = 1
EMAIL_BACKEND = mysettings.EMAIL['EMAIL_BACKEND']
EMAIL_USE_TLS = mysettings.EMAIL['EMAIL_USE_TLS']
EMAIL_PORT = mysettings.EMAIL['EMAIL_PORT']
EMAIL_HOST = mysettings.EMAIL['EMAIL_HOST']
EMAIL_HOST_PASSWORD = mysettings.EMAIL['EMAIL_HOST_PASSWORD']
REDIRECT_PAGE = mysettings.EMAIL['EMAIL_PAGE']
'''

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'testyb0210@gmail.com'
EMAIL_HOST_PASSWORD = 'vehiqbgfrsfylktd'
REDIRECT_PAGE = 'http://127.0.0.1:8000/account/signin/'
# https://support.google.com/accounts/answer/6010255
# 22/05/30 이후로 google에서 사용자 이름과 비밀번호로 로그인 요청하는 서드파티 앱 지원 안함
# 보안 수준 낮은 앱의 액세스 허용 이제 이거로 불가능
# kdevkr.github.io/gmail-smtp/ 참고

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
