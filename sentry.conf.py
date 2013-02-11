import os.path

CONF_ROOT = os.path.dirname(__file__)

# For Sentry on Openshift, choose either mysql or postgresql_psycopg2 for ENGINE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.environ['OPENSHIFT_APP_NAME'],  # Or path to database file if using sqlite3.
    }
}

try:
    env_db_name = {
        'django.db.backends.mysql': 'MYSQL',
        'django.db.backends.postgresql_psycopg2': 'POSTGRESQL'
    }[DATABASES['default']['ENGINE']]
except KeyError:
    import sys
    sys.exit("Please set the database engine to django.db.backends.mysql or django.db.backends.postgresql_psycopg2 for this Sentry Openshift setup.")

DATABASES['default'].update({
    'USER': os.environ['OPENSHIFT_%s_DB_USERNAME' % env_db_name ],      # Not used with sqlite3.
    'PASSWORD': os.environ['OPENSHIFT_%sL_DB_PASSWORD' % env_db_name],  # Not used with sqlite3.
    'HOST': os.environ['OPENSHIFT_%s_DB_HOST' % env_db_name],           # Set to empty string for localhost. Not used with sqlite3.
    'PORT': os.environ['OPENSHIFT_%s_DB_PORT' % env_db_name],           # Set to empty string for default. Not used with sqlite3.
})


# Edit this!
SENTRY_KEY = 'super_secret_key'

# Set this to false to require authentication
SENTRY_PUBLIC = False

# You should configure the absolute URI to Sentry. It will attempt to guess it if you don't
# but proxies may interfere with this.
# SENTRY_URL_PREFIX = 'http://sentry.example.com'  # No trailing slash!

SENTRY_WEB_HOST = os.environ['OPENSHIFT_INTERNAL_IP']
SENTRY_WEB_PORT = os.environ['OPENSHIFT_INTERNAL_PORT']
SENTRY_WEB_OPTIONS = {
    'workers': 3,  # the number of gunicorn workers
    # 'worker_class': 'gevent',
    'daemon':True,
    'pid': '%s/%s' % (os.environ['OPENSHIFT_DATA_DIR'],'gunicorn.pid'), # gunicorn pid file
    'log-file': '%s/%s' % (os.environ['OPENSHIFT_DIY_LOG_DIR'],'gunicorn_out.log'), # gunicorn the Error log file
    #'access-logfile': '%s%s' % (os.environ['OPENSHIFT_DIY_LOG_DIR'],'gunicorn_access.log'), # gunicorn the Error log file

}
# Mail server configuration

# For more information check Django's documentation:
#  https://docs.djangoproject.com/en/1.3/topics/email/?from=olddocs#e-mail-backends

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'localhost'
EMAIL_HOST_PASSWORD = ''
EMAIL_HOST_USER = ''
EMAIL_PORT = 25
EMAIL_USE_TLS = False

# http://twitter.com/apps/new
# It's important that input a callback URL, even if its useless. We have no idea why, consult Twitter.
TWITTER_CONSUMER_KEY = ''
TWITTER_CONSUMER_SECRET = ''

# http://developers.facebook.com/setup/
FACEBOOK_APP_ID = ''
FACEBOOK_API_SECRET = ''

# http://code.google.com/apis/accounts/docs/OAuth2.html#Registering
GOOGLE_OAUTH2_CLIENT_ID = ''
GOOGLE_OAUTH2_CLIENT_SECRET = ''

# https://github.com/settings/applications/new
GITHUB_APP_ID = ''
GITHUB_API_SECRET = ''

# https://trello.com/1/appKey/generate
TRELLO_API_KEY = ''
TRELLO_API_SECRET = ''
