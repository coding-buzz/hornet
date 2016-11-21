import os

from base import *


SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = True
ALLOWED_HOSTS = ['*']

COMPRESS_CSS_FILTERS = (
    'django_compressor_autoprefixer.AutoprefixerFilter',
)
COMPRESS_AUTOPREFIXER_BINARY = os.path.join(BASE_DIR, '..', 'node_modules/postcss-cli/bin/postcss')
COMPRESS_AUTOPREFIXER_ARGS   = ' --use autoprefixer'
COMPRESS_ENABLED = True
BASE_URL = 'http://coding.buzz'

MAILCHIMP_SEND_EMAILS = True
MAILCHIMP_API_KEY = os.environ['MAILCHIMP_API_KEY']
MAILCHIMP_SUB_LIST_NAME = 'Coding Buzz Subscriptions'
MAILCHIMP_SUBSCRIPTION_FORM_URL = os.environ['MAILCHIMP_SUBSCRIPTION_FORM_URL']

RECAPTCHA_PUBLIC_KEY = os.environ['RECAPTCHA_PUBLIC_KEY']
RECAPTCHA_PRIVATE_KEY = os.environ['RECAPTCHA_PRIVATE_KEY']
