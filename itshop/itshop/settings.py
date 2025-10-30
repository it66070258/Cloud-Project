from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SETTINGS_PATH = os.path.dirname(os.path.dirname(__file__))

TEMPLATE_DIRS = (
    os.path.join(SETTINGS_PATH, 'templates'),
)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-0$o!^6g@8%o#1)ao543)!55nh8123ugbc_#9r@a1u7u28@&7=-'

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
    'django.contrib.humanize',
    'shop',
    'ckeditor',
    'storages',
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

ROOT_URLCONF = 'itshop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'itshop.wsgi.application'


# Database

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "itshop",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "gg-db.cdsyamyv62ng.us-east-1.rds.amazonaws.com",
        "PORT": "5432",
    }
}


# Password validation

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

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Undo', 'Redo'],
            ['Bold', 'Italic', 'Underline', 'Strike', 'RemoveFormat'],
            ['FontSize', 'TextColor', 'BGColor'],
            ['NumberedList', 'BulletedList', 'Outdent', 'Indent'],
            ['Blockquote', 'SpecialChar'],
            ['Link', 'Unlink'],
            ['Image', 'Table', 'HorizontalRule'],
            ['Source', 'Maximize'],
        ],
        'height': 380,
        'width': '100%',
    }
}


# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = "Asia/Bangkok"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# --- AWS S3 Config ---
AWS_STORAGE_BUCKET_NAME = 'giga-gadget-s3'
AWS_S3_REGION_NAME = 'us-east-1'
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
AWS_S3_VERIFY = True

AWS_ACCESS_KEY_ID = '' # ว่างเพื่อใช้ IAM Role จาก EC2
AWS_SECRET_ACCESS_KEY = ''


STATIC_URL = f'https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/static/'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

MEDIA_URL = f'https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/media/'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

LOGIN_URL = "/login/"

# Default primary key field type

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
