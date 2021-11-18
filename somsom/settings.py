import os
from pathlib import Path
import json
from django.core.exceptions import ImproperlyConfigured


BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# json 파일에서 불러오기 / 21.04.02_dongmin
secret_file = os.path.join(BASE_DIR, 'secrets.json')

with open(secret_file) as f:
    secrets = json.loads(f.read())


def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {0} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)


SECRET_KEY = get_secret("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "localhost", "54.180.155.194"]


# Application definition

DJANGO_APPS = [
    'django.contrib.admin',         # 관리용 사이트
    'django.contrib.auth',          # 인증 시스템
    'django.contrib.contenttypes',  # 컨텐츠 타입을 위한 프레임워크
    'django.contrib.sessions',      # 세션 프레임워크
    'django.contrib.messages',      # 메세징 프레임워크
    'django.contrib.staticfiles',   # 정적 파일을 관리하는 프레임워크
    'corsheaders',
]

PROJECT_APPS = [
    'eggmorning.apps.EggmorningConfig',
    'users.apps.UsersConfig',
]

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'somsom.urls'

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

WSGI_APPLICATION = 'somsom.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'EGGMORNING',
        'USER': 'somadmin',
        'PASSWORD': 'L2dVfdeVn!',
        'HOST': 'eggmorning-db-20200722.ccgx9jpnb7kq.ap-northeast-2.rds.amazonaws.com',
        'PORT': 3306
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

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
]

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'ko'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

# 왜 없는지 확인 필요 21.04.02
# STATIC_ROOT = BASE_DIR / 'static'
# ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]', '.pythonanywhere.com']
# 테스트
# STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'))

# cors
CORS_ALLOW_ALL_ORIGINS = True

LOGIN_URL = '/users/login/'          # 로그인 URL
LOGIN_REDIRECT_URL = '/users/main/'  # 로그인 후 URL
LOGOUT_REDIRECT_URL = '/'            # 로그아웃 후 URL
# User Custom
AUTH_USER_MODEL = 'eggmorning.User'  # 커스텀 인증 모델
