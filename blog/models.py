from __future__ import unicode_literals

from django.db import models

import utils


class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)
    featured_image = models.ImageField(upload_to=utils.upload_directory_path)
    short = models.TextField()
    content = models.TextField()
    categories = models.ManyToManyField(Category)

    class Meta:
        ordering = ['-published_at']

    def __unicode__(self):
        return self.title


class ContentImage(models.Model):
    image = models.ImageField(upload_to=utils.upload_directory_path)
    title = models.CharField(max_length=255)
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='images')


class SourceCode(models.Model):
    _LANGUAGE_CHOICES = utils.get_available_lexers()

    language = models.CharField(max_length=40, choices=_LANGUAGE_CHOICES)
    content = models.TextField()
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='source_codes')
