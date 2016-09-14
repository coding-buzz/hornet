import os

from base import *


SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = False
ALLOWED_HOSTS = ['coding.buzz']


COMPRESS_CSS_FILTERS = (
    'compressor.filters.cssmin.rCSSMinFilter',
)
COMPRESS_ENABLED = True
