"""
Django settings for epsilonpos project.

Generated by 'django-admin startproject' using Django 3.0.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from tkinter.tix import Tree

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_+($v8+m9z94kh4*dpz-xc%nd#11^gf9xp$rb^=@g7#l8_k46+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda r: False,  # disables it
    # '...
}

ALLOWED_HOSTS = ['0.0.0.0','localhost','127.0.0.1']

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'django.contrib.humanize',

    'accounts',
    'inventory',
    'pos',
    'reports',
    'quotations',
    'expenses',

    'djmoney',
    'crispy_forms',
    'rest_framework',
    'jsonify',
    'bootstrap_modal_forms',
    'widget_tweaks',
    'sweetify',
    'django_countries',
    'django_filters',
    'dynamic_fields',
    'constance',
    'qrcode',
    # 'barcode',
    'phonenumber_field',
    'debug_toolbar',

    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'epsilonpos.urls'

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
                'expenses.context_processors.expense_form_processor'
            ],
        },
    },
]

WSGI_APPLICATION = 'epsilonpos.wsgi.application'

AUTH_USER_MODEL = 'accounts.CustomUser' # changes the built user model to ours



# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db_pinktouchie.sqlite3'),
#     }
# }
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.environ.get('POSTGRES_NAME'),
#         'USER': os.environ.get('POSTGRES_USER'),
#         'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
#         'HOST': 'db',
#         'PORT': 5432,
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'pink_touch_pos',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
        'OPTIONS': {  
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"  
        }  
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Maseru'

USE_I18N = True

USE_THOUSAND_SEPERATOR = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'accounts/static/')
]
MEDIA_URL = '/images/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'accounts/static/images')

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_URL = 'login'
LOGOUT_URL ='logout'
LOGIN_REDIRECT_URL ='system_dashboard'

CURRENCIES = ('MWK',)

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    # 'PAGE_SIZE': 10
}

CONSTANCE_ADDITIONAL_FIELDS = {
'image_field': ['django.forms.ImageField', {}],
'float_field': ['django.forms.FloatField', {}],
'boolean_field': ['django.forms.BooleanField', {}],
'yes_no_null_select': ['django.forms.fields.ChoiceField', {'widget': 'django.forms.Select','choices': (("yes", "Yes"), ("no", "No"))
}],
}

CONSTANCE_CONFIG = {
'SHOP_NAME':('EPSILON BAR','You are Home!!' ),
'TAG_LINE':('The best in Town!!', 'The best Shop in Town'),
'ADDRESS':('P.O. Box 418','Address' ),
'LOCATION':('Lilongwe','Lilongwe' ),
'COUNTRY':('Malawi','Malawi' ),
'TEL':('+ 265 000 000',' Tel'),
'FAX':('+ 265 000 000',' Fax'),
'CEL':('+ 265 000 000',' Cel'),
'EMAIL':('mcatechmw@mcatech.mw','MCATECH'),
'TAX_NAME':(16.5,'VAT','float_field'),
'LOGO_IMAGE': ('images.png', 'Company logo', 'image_field'),
'ABTN_50_499':(20.0,'AFEE 1','float_field'),
'ABTN_500_999':(38.0,'AFEE 2','float_field'),
'ABTN_1000_2499':(80.0,'AFEE 3','float_field'),
'ABTN_2500_4999':(160.0,'AFEE 4','float_field'),
'ABTN_5000_9999':(350.0,'AFEE 5','float_field'),
'ABTN_10000_14999':(600.0,'AFEE 6','float_field'),
'ABTN_15000_19999':(720.0,'AFEE 7','float_field'),
'ABTN_20000_24999':(920.0,'AFEE 8','float_field'),
'ABTN_25000_29999':(1050.0,'AFEE 9','float_field'),
'ABTN_30000_39999':(1250.0,'AFEE 10','float_field'),
'ABTN_40000_49999':(1500.0,'AFEE 11','float_field'),
'ABTN_50000_59999':(1900.0,'AFEE 12','float_field'),
'ABTN_60000_79999':(2300.0,'AFEE 13','float_field'),
'ABTN_80000_99999':(2750.0,'AFEE 14','float_field'),
'ABTN_100000_124999':(3250.0,'AFEE 15','float_field'),
'ABTN_125000_149999':(3500.0,'AFEE 16','float_field'),
'ABTN_150000_199999':(3750.0,'AFEE 17','float_field'),
'ABTN_200000_299999':(4500.0,'AFEE 18','float_field'),
'ABTN_300000_399999':(5500.0,'AFEE 19','float_field'),
'ABTN_400000_ABOVE':(7000.0,'AFEE 20','float_field'),

'BTN_50_500':(30.0,'FEE 1','float_field'),
'BTN_501_900':(35.0,'FEE 2','float_field'),
'BTN_901_1000':(37.0,'FEE 3','float_field'),
'BTN_1001_2400':(80.0,'FEE 4','float_field'),
'BTN_2401_2500':(150.0,'FEE 5','float_field'),
'BTN_2501_4900':(160.0,'FEE 6','float_field'),
'BTN_4901_5000':(340.0,'FEE 7','float_field'),
'BTN_5001_9900':(350.0,'FEE 8','float_field'),
'BTN_9901_10000':(580.0,'FEE 9','float_field'),
'BTN_10001_14900':(340.0,'FEE 10','float_field'),
'BTN_10001_14900':(600.0,'FEE 11','float_field'),
'BTN_14901_15000':(700.0,'FEE 12','float_field'),
'BTN_15001_15900':(720.0,'FEE 13','float_field'),
'BTN_15901_20000':(900.0,'FEE 14','float_field'),
'BTN_20001_25000':(1000.0,'FEE 15','float_field'),
'BTN_25001_30000':(1200.0,'FEE 16','float_field'),
'BTN_30001_40000':(1450.0,'FEE 17','float_field'),
'BTN_40001_50000':(1850.0,'FEE 18','float_field'),
'BTN_50001_60000':(2200.0,'FEE 19','float_field'),
'BTN_60001_80000':(2650.0,'FEE 20','float_field'),
'BTN_80001_100000':(3200.0,'FEE 21','float_field'),
'BTN_100001_125000':(3400.0,'FEE 22','float_field'),
'BTN_125001_150000':(3700.0,'FEE 23','float_field'),
'BTN_150001_200000':(4500.0,'FEE 24','float_field'),
'BTN_200001_300000':(4900.0,'FEE 25','float_field'),
'BTN_300001_400000':(4900.0,'FEE 26','float_field'),
'BTN_400001_500000':(6900.0,'FEE 27','float_field'),
'BTN_500001_600000':(6900.0,'FEE 28','float_field'),
'BTN_600001_750000':(6900.0,'FEE 29','float_field'),
'ACCOUNT_NUMBER':('1234567890','ACCOUNT NUMBER'),
'QUICK_SALE': ('yes', 'QUICK_SALE', 'yes_no_null_select'),
}

CONSTANCE_CONFIG_FIELDSETS = {
'Shop Options': ('SHOP_NAME','LOGO_IMAGE','TAG_LINE','ADDRESS','LOCATION','TEL','FAX','EMAIL','CEL','COUNTRY'),
'Invoice Options': ('TAX_NAME',),
'Pos Settings':('QUICK_SALE','ACCOUNT_NUMBER',),

'Airtel Money Fees':(
'ABTN_50_499',
'ABTN_500_999',
'ABTN_1000_2499',
'ABTN_2500_4999',
'ABTN_5000_9999',
'ABTN_10000_14999',
'ABTN_15000_19999',
'ABTN_20000_24999',
'ABTN_25000_29999',
'ABTN_30000_39999',
'ABTN_40000_49999',
'ABTN_50000_59999',
'ABTN_60000_79999',
'ABTN_80000_99999',
'ABTN_100000_124999',
'ABTN_125000_149999',
'ABTN_150000_199999',
'ABTN_200000_299999',
'ABTN_300000_399999',
'ABTN_400000_ABOVE',
),

'Mbamba Money Fees':(
'BTN_50_500',
'BTN_501_900',
'BTN_901_1000',
'BTN_1001_2400',
'BTN_2401_2500',
'BTN_2501_4900',
'BTN_4901_5000',
'BTN_5001_9900',
'BTN_9901_10000',
'BTN_10001_14900',
'BTN_14901_15000',
'BTN_15001_15900',
'BTN_15901_20000',
'BTN_20001_25000',

'BTN_25001_30000',
'BTN_30001_40000',
'BTN_40001_50000',
'BTN_50001_60000',
'BTN_60001_80000',
'BTN_80001_100000',
'BTN_100001_125000',
'BTN_125001_150000',
'BTN_150001_200000',
'BTN_200001_300000',
'BTN_300001_400000',
'BTN_400001_500000',
'BTN_500001_600000',
'BTN_600001_750000',)
}

PHONENUMBER_DB_FORMAT = 'NATIONAL'
PHONENUMBER_DEFAULT_REGION = 'MW'

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'