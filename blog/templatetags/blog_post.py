import re
from django import template
from django.core.exceptions import ObjectDoesNotExist

from blog.models import ContentImage


register = template.Library()

_IMAGE_TAG_REGEX = re.compile(r'{{ image \d+ }}')
_IMAGE_HTML_TAG = '<img src="{path}" alt="{title}"/>'

_YOUTUBE_TAG_REGEX = re.compile(r'{{ youtube .+ }}')
_YOUTUBE_HTML_TAG = '<iframe class="yt-frame" type="text/html" src="http://www.youtube.com/embed/{movie_id}"></iframe>'


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
def include_all_elements(post_content):
    post_content = include_images(post_content)
    post_content = include_youtube(post_content)
    return post_content
