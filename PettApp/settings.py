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

ALLOWED_HOSTS = ["*"]


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
    'location',
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
        "USER": "hashiq",
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
  "project_id": "petapp-7f76a",
  "private_key_id": "6a940c9780951e27bf6da2fae1b6e56ef393688d",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDtCKQk5HGnezTq\nXvRsKc1Zs9ZUT00wY4LuCU5oCDfrci6mZm8iT4dYoaFPWp9MhoLJvphsbWeG5CYy\ncnu/EBxpxpB8Nw0W45+vqnKAw+HDS31CIKWHxAQ6Absd7xV9GyYBlK4SRdqsXijz\nUXFRRJ38W/dZ5AqdFsQOLyMHW/qWoOpyExsBu0/B+H35lR7lBijLQf1+KDJ94glX\n2d4ivZatZaXUK2fqtyfCyE4jsE1593E/jshPs3UU488iMdKoZiTpyiW2FagsRkjm\n9Ysi2/NUUuUHsLj2aFXFe+Sab/9quGEYO1/oJNkyIzc64vI2R7gyCSYx80BMUXZf\noiNAHnsJAgMBAAECggEAIwku8gEOR5ovhSEJ8d7v6n1phca++xMKbFLV0wy770JO\nYOwtKx4kPFaPuGIFv9L2DAnvD7/QGKEqgDRp1CD2gjAGdUXR2ntExDtmd1/8w9gp\nqJeYwAuaMFTHKrKHM5nKsVsfq7XFj8rPNL/qBwAkdgPF+PR7GSMfUZVoERNoY9EW\nY6CMA+1y++l4T+HM09hytzluqRQuu6KrI9E+AcOO85Eq59f27DnQxILfFhAPC6l9\nE/2k0eNXeRlp4xdcQmpMKBYZeqGpZS74mPouYedK2XJaU6MDSlWyMOOMhdxrDyhL\n5s2B2KGmYfR6TjySSOO+Y5fm79jnDzqALR9XevxNcQKBgQD3WtvGYN0MN95dwIhf\np0Ha+JPuRHwwjhY3pQJMeZVFGTIGrpWiQIp8CV0MYHXKZn1Ejn7LwAeGHJaHlqSg\nE9QwUPme33hhB5E7wDnrIcIaAHXcRxvnPjJeeZi1VFDIFsG6jRbQ7+s1ECLrGXTA\nKYQNN7CgHXoeQ9mKolDbtbP1XQKBgQD1UW/XYKNOoRut3Pl9QxJGlzA+JXxWgipo\nbSS9sDLYHcdB/aFuxGWso/7+0wc2yci/2hWzKK4/4NZpEV9IyPynPAWhYNnmsDTi\nqGP04tm3ezVHzspIhuXnej9g0GP0jsfs/ujQ4BWDy+Dyp95kOQ42KTGHl8tFY6Cb\nphMHDLv1nQKBgHzGHWTlibvXFtmN/Hzb3zF5AQ5JB6hqlDR/jThMgIq5me2a9apC\nClllU8WhhumRZ5FEnBtlg6YYF6rPx71kIz44KqMEsTGo4o8UeWLtxX7eSpXSXPX5\n/uh/SBP4M0Orjw/uidrdm3VJ7YNQdP9WMeGE/RjXpblMmpj/JfCeqOeVAoGBALLn\nCvs0/KOxFnB7AG97ZG6af5Iy4DRuhOLXBb5YKxw0y0Wy4/HVxJhcmO/Zkh9AlOhk\n8QJRHpJzM6o4AxcfjDGhsjF4YjC8PDU3vH2wmjoW3kpZ4md2CWAAZQwDrYGCRwbs\n93isksQlAQ21opfQjC6vZ/GMn68g8tXQDXxMqx55AoGALuxPBp/Onm2e/5ZmQ5aR\noW6jg15Fl0tBUC0CnCg+oHXPU9qLnZXCU/u4tFkMPwK82fSAoqBjIgSCyBOT7iln\nEpy1jKgztzaFLqWwsWiVQs+wnlf1JaR6RcXmfBeLutG4aN8m98RXJLkRRJVa5yI8\nh+iE5p6MuPGdHhabKjP4NNk=\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-bvw51@petapp-7f76a.iam.gserviceaccount.com",
  "client_id": "114896707277965395715",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-bvw51%40petapp-7f76a.iam.gserviceaccount.com"
}




# Firebase Initializing #
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
cred = credentials.Certificate(serviceAccountKey)
firebase_admin.initialize_app(cred)
