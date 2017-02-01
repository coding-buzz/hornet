import re

from django import template
from django.core.exceptions import ObjectDoesNotExist
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from repoze.lru import lru_cache

from blog.models import ContentImage, SourceCode


register = template.Library()

_IMAGE_TAG_REGEX = re.compile(r'{{ image \d+ }}')
_IMAGE_HTML_TAG = '<a href="{path}" target="_blank"><img src="{path}" alt="{title}"/></a>'

_YOUTUBE_TAG_REGEX = re.compile(r'{{ youtube .+ }}')
_YOUTUBE_HTML_TAG = '<iframe class="yt-frame" type="text/html" src="http://www.youtube.com/embed/{movie_id}"></iframe>'

_SOURCE_CODE_TAG_REGEX = re.compile(r'{{ sourcecode \d+ }}')


@register.filter
def include_images(post_content):
    for image_tag in re.findall(_IMAGE_TAG_REGEX, post_content):
        try:
            image_id = image_tag.lstrip('{{ image ').rstrip(' }}')
            content_image = ContentImage.objects.get(id=image_id)
            image_html_tag = _IMAGE_HTML_TAG.format(path=content_image.image.url, title=content_image.title)
            post_content = post_content.replace(image_tag, image_html_tag)
        except ObjectDoesNotExist:
            pass
    return post_content


@register.filter
def include_youtube(post_content):
    for youtube_tag in re.findall(_YOUTUBE_TAG_REGEX, post_content):
        try:
            movie_id = youtube_tag.lstrip('{{ youtube ').rstrip(' }}')
            youtube_html_tag = _YOUTUBE_HTML_TAG.format(movie_id=movie_id)
            post_content = post_content.replace(youtube_tag, youtube_html_tag)
        except ObjectDoesNotExist:
            pass
    return post_content


@register.filter
def include_source_codes(post_content):
    for source_code_tag in re.findall(_SOURCE_CODE_TAG_REGEX, post_content):
        try:
            source_code_id = source_code_tag.lstrip('{{ sourcecode ').rstrip(' }}')
            source_code = SourceCode.objects.get(id=source_code_id)
            lexer = get_lexer_by_name(source_code.language)
            formatted_code = highlight(source_code.content, lexer, HtmlFormatter(linenos=True))
            formatted_code = "<div class='source-code-wrapper'>{}</div>".format(formatted_code)
            post_content = post_content.replace(source_code_tag, formatted_code)
        except ObjectDoesNotExist:
            pass
    return post_content


@register.filter
def include_all_elements(post_content):
    post_content = include_images(post_content)
    post_content = include_youtube(post_content)
    post_content = include_source_codes(post_content)
    return post_content


@register.simple_tag
@lru_cache(maxsize=1)
def get_pygments_styles():
    return HtmlFormatter(style='tango').get_style_defs('.highlight')
