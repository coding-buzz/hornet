import os

from base import *


SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = False
ALLOWED_HOSTS = ['coding.buzz']

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
