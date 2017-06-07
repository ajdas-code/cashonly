"""
Django settings for cashonly project.

Generated by 'django-admin startproject' using Django 1.10.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+mr!12odk72qsa&=$ydx5^@c(hz_=*qai@s3fu_sdv!o^(7jzd'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '.elasticbeanstalk.com',
    'localhost',
    '127.0.0.1',
    '.cashon.ly',
    '.pythonanywhere.com'
]

INTERNAL_IPS = (
    '0.0.0.0',
    '127.0.0.1',
)

ADMINS = [
    ('Haldun Anil', 'haldun@cashon.ly')
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'storages',
    'phonenumber_field',
    'accounts',
    'transactions',
    'django_extensions',
    'social_django',
    'django_countries',
    'tinymce',
    'appconfig',
    'simple_history',
    'mathfilters',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
]

ROOT_URLCONF = 'cashonly.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'cashonly.wsgi.application'

LOGIN_REDIRECT_URL = '/'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

# mysql-- to be used on pythonaywhere
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'haldunanil$codb',
        'USER': 'haldunanil',
        'PASSWORD': '$$Ca$hcmhaja19',
        'HOST': 'haldunanil.mysql.pythonanywhere-services.com',
        'TEST': {
            'NAME': 'haldunanil$test_codb'
        }
    }
}

# postgres-- to be used on AWS
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'codb',
#         'USER': 'postgres',
#         'PASSWORD': '$$Ca$hcmhaja19',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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

# Social authentication backend settings
AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',

    # Make up a username for this person, appends a random string at the end if
    # there's any collision.
    # 'social_core.pipeline.user.get_username',

    # CUSTOM: this gets email address as the username and validates it matches
    # the logged in user's email address.
    'accounts.pipeline.get_username',

    # 'social_core.pipeline.mail.mail_validation',
    'social_core.pipeline.social_auth.associate_by_email',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
    'accounts.pipeline.add_to_group',
)

SOCIAL_AUTH_URL_NAMESPACE = 'social'

LOGIN_URL = 'sign-in'
LOGOUT_URL = 'sign-out'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

# social auth Facebook params
SOCIAL_AUTH_FACEBOOK_KEY = '1956887344534145'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '2b6e54f57521524014fe38e8d89a3cbf'  # App Secret

SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
   'fields': 'id, name, email, age_range'
}
SOCIAL_AUTH_FACEBOOK_AUTH_EXTRA_ARGUMENTS = {
    # 'auth_type': 'reauthenticate',
}

# social auth Google params
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '286698641076-bdfl2p9qfkl0bs8pl1o16dqnu873v9n3.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'VrdEHGJnmtI13DOdERV4jurP'

# social auth generic params
SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = True
SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/sign-up/more-details/'

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "static")

STATICFILES_DIRS = ( os.path.join('assets'), )

STATIC_URL = '/static/'

# Security
# https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

CSRF_COOKIE_SECURE = True

SESSION_COOKIE_SECURE = True

SECURE_SSL_REDIRECT = True

X_FRAME_OPTIONS = 'DENY'

# Enabling flatpages and TinyMCE
# https://docs.djangoproject.com/en/1.10/ref/contrib/flatpages/
# https://django-tinymce.readthedocs.io/en/latest/installation.html#configuration

SITE_ID = 1

TINYMCE_DEFAULT_CONFIG = {
        'plugins': "table,spellchecker,paste,searchreplace",
        'theme': "advanced",
        'cleanup_on_startup': True,
        'custom_undo_redo_levels': 10, }

TINYMCE_SPELLCHECKER = True

# TINYMCE_COMPRESSOR = True

# Stripe
# https://dashboard.stripe.com/account/apikeys
STRIPE_API_TEST_SECRET = 'sk_test_iLOI0zuwgnqGncXfEq0SKNNp'
STRIPE_API_TEST_PUBLIC = 'pk_test_ntvPJgeDpYjjf0OUmmL3RY75'

STRIPE_API_PROD_SECRET = ''
STRIPE_API_PROD_PUBLIC = ''
