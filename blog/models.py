from __future__ import unicode_literals
import uuid

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
    publication_notified = models.BooleanField(default=False)
    featured_image = models.ImageField(upload_to=utils.upload_directory_path)
    short = models.TextField()
    content = models.TextField()
    categories = models.ManyToManyField(Category)
    preview_key = models.CharField(max_length=100, default=utils.generate_preview_key)

    class Meta:
        ordering = ['-published_at']

    def __unicode__(self):
        return (self.title[:30] + '...') if len(self.title) > 30 else self.title


class ContentImage(models.Model):
    image = models.ImageField(upload_to=utils.upload_directory_path)
    title = models.CharField(max_length=255)
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='images')


class SourceCode(models.Model):
    _LANGUAGE_CHOICES = utils.get_available_lexers()

    language = models.CharField(max_length=40, choices=_LANGUAGE_CHOICES)
    content = models.TextField()
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='source_codes')


class Comment(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']

    def get_anchor_name(self):
        return 'comment-{}'.format(self.id)
