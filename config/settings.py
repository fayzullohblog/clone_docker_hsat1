"""
# # https://docs.djangoproject.com/en/4.2/topics/settings/
# # https://docs.djangoproject.com/en/4.2/topics/settings/
# # https://docs.djangoproject.com/en/4.2/topics/settings/
# # https://docs.djangoproject.com/en/4.2/topics/settings/
# # https://docs.djangoproject.com/en/4.2/topics/settings/
# # https://docs.djangoproject.com/en/4.2/topics/settings/
# # https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from decouple import config
import os




BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))




# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = config('DEBUG',default=False,cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=lambda v: [s.strip() for s in v.split(',')])









# Application definition

INSTALLED_APPS = [
    'jazzmin',
    # "daphne",   # for channels notification
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'whitenoise.runserver_nostatic',
]


OUT_APPS=[
    'rest_framework_swagger',       # Swagger 
    'rest_framework',
    'drf_yasg',
    'rest_framework.authtoken',
    'rest_framework_simplejwt.token_blacklist',
    'corsheaders',   # xafsizlik ucghun, biz qaysi domenlardan request kelishini ta'mnlab beradi

    'decouple',
    'tinymce',
    'debug_toolbar',   # loyhani ishlash holatini ko'rish uchun
    # 'wkhtmltopdf',  #pDFKIT uchun
]

MY_APP=[
    'accountapp.apps.AccountappConfig',
    'letterapp.apps.LetterappConfig',
    'letterinstructionapp.apps.LetterinstructionappConfig',
    'mainletter.apps.MainletterConfig',
    'lettersummonapp.apps.LettersummonappConfig',
    'lettercourtapp.apps.LettercourtappConfig',
    'signedletter.apps.SignedletterConfig',
]



INSTALLED_APPS=INSTALLED_APPS+OUT_APPS+MY_APP

REST_FRAMEWORK={
    'DEFAULT_AUTHENTICATION_CLASSES':[
            'rest_framework_simplejwt.authentication.JWTAuthentication',  # SestionAuthenticatio and TokenAuthenticationlarni ham ko'rish
    ],

    'DEFAULT_PERMISSION_CLASSESS':[
        'rest_framework.permissions.djangoModelPermissionsOrAnonReadOnly'
    ],
    
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100,
    
}


SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'basic': {
            'type': 'basic'
        }
    },
    
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',     # debug_toolbar uchun qushilgan
]


CORS_ALLOWED_ORIGINS = [
    "https://reportx.hsat.uz",  # Loyhamning manzili manzili
    "http://localhost:5173",
    "http://localhost:5174",   # Localhost manzili 
    'https://statistics-front.vercel.app',
]

CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# CHANNEL_LAYERS = {
#     'default': {
#         'BACKEND': "channels.layers.InMemoryChannelLayer"
#     }
# }
# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR ,'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'testdatabase', # PostgreSQL ma'lumotlar bazasi nomi
        'USER': 'testusername', # PostgreSQL foydalanuvchi nomi
        'PASSWORD': 'testpassword', # PostgreSQL foydalanuvchi paroli
        'HOST': 'localhost', # Ma'lumotlar bazasining joylashgan manzili
        'PORT': '5432', # Ma'lumotlar bazasi porti (standart port bo'lsa, qoldiring)
    }
}





# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]





# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS=[os.path.join(BASE_DIR,'static')]
STATIC_ROOT=os.path.join(BASE_DIR,'staticfiles')


# django 4.2+ whitenoise 
STORAGES = {
    # ...
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}



STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]
# settings.py

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')


AUTH_USER_MODEL='accountapp.MyUser' 

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'




# Django project settings.py

from datetime import timedelta
import os


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=300),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN": False,

    "ALGORITHM": "HS256",
    
    "VERIFYING_KEY": "",
    "AUDIENCE": None,
    "ISSUER": None,
    "JSON_ENCODER": None,
    "JWK_URL": None,
    "LEEWAY": 0,

    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",

    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",

    "JTI_CLAIM": "jti",

    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),

    "TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainPairSerializer",
    "TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSerializer",
    "TOKEN_VERIFY_SERIALIZER": "rest_framework_simplejwt.serializers.TokenVerifySerializer",
    "TOKEN_BLACKLIST_SERIALIZER": "rest_framework_simplejwt.serializers.TokenBlacklistSerializer",
    "SLIDING_TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainSlidingSerializer",
    "SLIDING_TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSlidingSerializer",
}

DATA_UPLOAD_MAX_MEMORY_SIZE=5242880  ## % 5MB


# TINYMCE_JS_URL = os.path.join(STATIC_URL, "path/to/tiny_mce/tiny_mce.js")

TINYMCE_DEFAULT_CONFIG = {
    'custom_undo_redo_levels': 100,
    'selector': 'textarea',
    "menubar": "file edit view insert format tools table help",
    'plugins': 'link image preview codesample contextmenu table code lists fullscreen',
    'toolbar1': 'undo redo | backcolor casechange permanentpen formatpainter removeformat formatselect fontselect fontsizeselect',
    'toolbar2': 'bold italic underline blockquote | alignleft aligncenter alignright alignjustify '
               '| bullist numlist | outdent indent | table | link image | codesample | preview code | tiny_mce_wiris_formulaEditor tiny_mce_wiris_formulaEditorChemistry',
    'contextmenu': 'formats | link image',
    'block_formats': 'Paragraph=p; Header 1=h1; Header 2=h2',
    'fontsize_formats': "8pt 10pt 12pt 14pt 16pt 18pt",
    'content_style': "body { font-family: Arial; background: white; color: black; font-size: 12pt}",
    'codesample_languages': [
        {'text': 'Python', 'value': 'python'}, {'text': 'HTML/XML', 'value': 'markup'},],
    'image_class_list': [{'title': 'Fluid', 'value': 'img-fluid', 'style': {} }],
    'width': '700px',
    "height": "700px",
    'image_caption': True,
    "images_upload_url": "upload_image",
}


INTERNAL_IPS = [
    # ...  DEBUG_TOOLBAR
    "127.0.0.1",
    # ...
]





# WKHTMLTOPDF

WKHTMLTOPDF_CMD = '/path/to/my/wkhtmltopdf'

WKHTMLTOPDF_CMD_OPTIONS = {
    'quiet': True,
}