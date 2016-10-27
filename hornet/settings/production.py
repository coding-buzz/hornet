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