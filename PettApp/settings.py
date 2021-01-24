"""
Django settings for PettApp project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8ctx4pa10@+zug-nmq+#26yaz+of)kixp-elgx--*yih!k*wod'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["18.222.253.154"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # apps
    'account',
    'petdata',
    
    # Libraries #
    'rest_framework',
    'django_extensions',
    'django.contrib.gis',
    'leaflet',
   

]
AUTH_USER_MODEL = 'account.User' 
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'PettApp.urls'

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

WSGI_APPLICATION = 'PettApp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases


DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": "petapp",
        "USER": "postgres",
        "PASSWORD": "3134",
        "HOST": "localhost",
        "PORT": "5432",
    }
}


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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Firebase Credentials #
serviceAccountKey  = {
  "type": "service_account",
  "project_id": "petapp-6f293",
  "private_key_id": "38711df5b2fe1f5e1a906a7598aae1619d0e2f17",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCne5RkMAh/uU+2\nlRtTxGSRhLMn7BzOeIUECSo1jcQA/WXCm+WFzPg5ri3a+XtTg/PWODt7HpbPigip\nSiEymCOG0T8RKY2+Vhf2jdHpEIqzz5lox0rbsR+MniUZBGUBbVy0JIWDHPc4cJvS\nrVzTzrfQRxB7n2ycdOQghC1W0aOibGCjSrfqScVO0tYp6yhLspH7BC/7civIHwh4\nhW3uxeP+5f6nOvXy2v0sJSsbYoxX90lHJ5bi/dvTiaYs7p/gFFAdPZXrHUzxLOaH\nXyb0UXiIqN2yt3p1QeFl+H7R3KFo1zvayCeM7lhhYqYZglm6ZMW+N+z8LSdhLJSd\nEMJOYAmfAgMBAAECggEAN8IWQJaXNcKBjdUtUGGJY8LsjEV4v6pzCkls0oB8eSHj\nj3ssWjPHjhh1brnxO3gqJS76an5gEf8v7ABgdgIdjcQ6/WE6rdvmxXAoqrGVo9Bh\nD/eNbf+Vc9CwpBgI8oUwwE6KXoC1s4YV8nlB9sgS/RWzoJyOYbYuvr6Sg51un2Nw\nZPtkIzXESY/kxtaBPbC9mxPxTo/c5HMq8ggGWQLG+ZKI2qDRZrlrrJNMn/Gpoack\nSLMko5nBVNn+70r1CiF1VPG2WIYZCLv7czOEraUBRAmQ8lQa0rf7AxfaLUODQWkh\nV+PRSvgbLxf1J7ty0YgcMRa28qLCQnV5vy+4nbr6bQKBgQDaa/CXPVWIv4BKWBub\n1TUv/DnUHdLRsOzAAvf7rW1t0wexd/Nt2UFizSordHHTaF/tFL8SCRSr7YJm/cTa\n7KBwNbeV5RgMYVF1Ge603wcyNTcRxOY5Ki5KjRQFEIhZ4PONEixWt/ZE8zdKGe8M\nzp6pV8PucGY1zOmiKFRNQfBobQKBgQDETBxMX+RKjbyBH0COQvg8vR6QMI/sYEIT\nvWCfBdDeE34bqDeLfAmXZA4slNarBESK2A1TKI272Dbr0RUCbQUbr51Jeejc9gqG\nrhJdXEkMtbMyiuZ/BIP9f/NqJJJrA0bTMn+ha7NG1jwoiNKlsD8bRwDivXt0J6sY\nFpVyX72KuwKBgQC3MMyqrCBu/t5kfB07x8hCJLODuje080S9jj/acAxVjibnq4kZ\nWpvCd/ykUZeeDe5Wc44FXGRgBmXWZ4SRcODm+8asC2buCzk8k7FnNZ9ddtBnMNM+\noqgMkuJ1lPYnG8ppSRKy8Lu1/J8koTejcDAWK6wC8XZoLSLOhDCgU2uEyQKBgDsj\n9y6ngV9Y3p9EbC2wTZv3Gps0llgQFDhgSRkAJpKR6t+oSbvTjgw3j/GskhSKP6BZ\nQYJ5aGJc3QclQiAt+mkB+vBlM1xHIJq9HTlVkYirwaaLpLBGCwI4J30mMZreLNt6\njmtyyFuiNhO8TUKwHAM63DB0CBrRzMGAJFyGLdP7AoGAdYRuyJJODG1h9XY+vR2m\nCZMDzvuJaW0MpQZw1KPChFSy+d7pXf98ILICGLVljF8uvvo18lzYlGvDtG/sMSPe\n66h83LtKy9kQ9IkoTTF+IjQs8c5HJ9TnppTDfjh9mGGzuHwmwEAi/W0sCbltP/no\nnHmlqrO6m+dlIwluYmqcrCQ=\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-wwzwx@petapp-6f293.iam.gserviceaccount.com",
  "client_id": "107989114844905158794",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-wwzwx%40petapp-6f293.iam.gserviceaccount.com"
}



# Firebase Initializing #
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
cred = credentials.Certificate(serviceAccountKey)
firebase_admin.initialize_app(cred)