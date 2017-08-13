# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
            'default': {
                        'ENGINE': 'django.db.backends.postgresql_psycopg2',
                        'NAME': '',
                        'USER': '',
                        'PASSWORD': '',
                        'HOST': 'db',
                        'PORT': '5432',
                                                                    }
            }

EMAIL_USE_TLS = True
EMAIL_HOST = ''
EMAIL_PORT = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''

DISQUS_API_KEY = ''
DISQUS_WEBSITE_SHORTNAME = ''

TWITTER_API_KEY = ''
TWITTER_API_SECRET = '' 
TWITTER_API_OWNER_HANDLE = ''
TWITTER_API_OWNER_ID = ''
TWITTER_API_ACCESS_TOKEN = ''
TWITTER_API_TOKEN_SECRET = ''
TWITTER_API_CONSUMER_KEY = ''
TWITTER_API_CONSUMER_SECRET = ''
