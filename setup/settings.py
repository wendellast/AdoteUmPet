"""
Django settings for setup project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
from pathlib import Path

import dotenv

dotenv.load_dotenv(dotenv.find_dotenv())


BASE_DIR = Path(__file__).resolve().parent.parent


# TODO change secrect-key
SECRET_KEY = "django-insecure-6n@haxmlnd&u*gs*y2sbodhna43sbe++v3ex6lvcpp3ga_bkmk"

# TODO doenv
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False if os.environ.get("DEBUGDB") == "False" else True


ALLOWED_HOSTS = ["127.0.0.1", "adoteumpet.up.railway.app", ".vercel.app", ".now.sh"]

CSRF_TRUSTED_ORIGINS = [
    "http://127.0.0.1",
    "https://adoteumpet.up.railway.app",
]
# Application definition

INSTALLED_APPS = [
    "jazzmin",  # Theme Django-admin
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "uuid",
    # My Apps
    "pet",
    "adoption",
    "userauth",
    # Allauth
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "allauth.socialaccount.providers.facebook",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]


SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "APP": {
            "client_id": os.environ.get("CLIENT_ID"),
            "secret": os.environ.get("SECRET"),
            "key": "",
        },
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        },
        "OAUTH_PKCE_ENABLED": True,
    },
    "facebook": {
        "METHOD": "oauth2",  # Set to 'js_sdk' to use the Facebook connect SDK
        "SDK_URL": "//connect.facebook.net/{locale}/sdk.js",
        "SCOPE": ["email", "public_profile"],
        "AUTH_PARAMS": {"auth_type": "reauthenticate"},
        "INIT_PARAMS": {"cookie": True},
        "FIELDS": [
            "id",
            "first_name",
            "last_name",
            "middle_name",
            "name",
            "name_format",
            "picture",
            "short_name",
        ],
        "EXCHANGE_TOKEN": True,
        "LOCALE_FUNC": "path.to.callable",
        "VERIFIED_EMAIL": False,
        "VERSION": "v13.0",
        "GRAPH_API_URL": "https://graph.facebook.com/v13.0",
    },
}


ROOT_URLCONF = "setup.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "setup.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": os.environ.get("DATABASE_ENGINE"),
        "NAME": os.environ.get("DATABASE_NAME"),
        "USER": os.environ.get("DATABASE_USER"),
        "PASSWORD": os.environ.get("DATABASE_PASSWORD"),
        "HOST": os.environ.get("DATABASE_HOST"),
        "PORT": os.environ.get("DATABASE_PORT"),
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


SOCIALACCOUNT_PIPELINE = (
    "allauth.socialaccount.pipeline.social_login",
    "userauths.pipeline.link_to_existing_user",  # Add this line
    "allauth.socialaccount.pipeline.social_user",
    "allauth.socialaccount.pipeline.associate_user",
    "allauth.socialaccount.pipeline.load_extra_data",
    "allauth.socialaccount.pipeline.user.create_user",
    "allauth.socialaccount.pipeline.save_social_token",
    "allauth.socialaccount.pipeline.social_account",
    "allauth.socialaccount.pipeline.sync_user_profile",
)

AUTH_USER_MODEL = "userauth.User"


LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

LOGIN_URL = "userauths:sign-in"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"
SITE_ID = 1


STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = [os.path.join(BASE_DIR, "templates/static")]

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"


EMAIL_HOST = os.environ.get("EMAIL_HOST")
EMAIL_POST = os.environ.get("EMAIL_POST")
EMAIL_USE_TLS = os.environ.get("EMAIL_USE_TLS")
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")


JAZZMIN_UI_TWEAKS = {
    "theme": "darkly",
}
