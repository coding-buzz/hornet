import re
from django import template
from django.core.exceptions import ObjectDoesNotExist

from blog.models import ContentImage


register = template.Library()

_IMAGE_TAG_REGEX = re.compile(r'{{ image \d+ }}')
_IMAGE_HTML_TAG = '<img src="{path}" alt="{title}"/>'


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
