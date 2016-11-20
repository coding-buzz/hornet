from django import forms
from django.contrib import admin
from django.shortcuts import redirect
from django.core import urlresolvers

from ckeditor.widgets import CKEditorWidget
from django_object_actions import DjangoObjectActions

import models
import views

class ContentImageInline(admin.StackedInline):
    model = models.ContentImage
    readonly_fields = ('id', )
    extra = 1


class SourceCodeInline(admin.StackedInline):
    model = models.SourceCode
    readonly_fields = ('id', )
    extra = 1


class CommentInline(admin.TabularInline):
    model = models.Comment
    readonly_fields = ('id', 'created_at', 'name', 'content', 'link_to_comment')
    extra = 0

    def link_to_comment(self, obj):
        link = urlresolvers.reverse("admin:blog_comment_change", args=[obj.id])
        return u'<a href="%s">[LINK]</a>' % (link)
        return 'foo2'

    link_to_comment.allow_tags = True


class BlogPostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        exclude = ['created_at']
        model = models.BlogPost


class BlogPostAdmin(DjangoObjectActions, admin.ModelAdmin):
    form = BlogPostForm
    filter_horizontal = ('categories', )
    inlines = (ContentImageInline, SourceCodeInline, CommentInline)

    def preview(self, request, obj):
        response = redirect('blog:blog_post_view', blog_post_id=obj.id)
        response['Location'] += '?preview_key={}'.format(obj.preview_key)
        return response

    change_actions = ('preview', )


admin.site.register(models.BlogPost, BlogPostAdmin)


class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Category, CategoryAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_filter = ['blog_post']
    list_display = ['name', 'link_to_blog_post', 'created_at']
    readonly_fields = ['link_to_blog_post', 'created_at']

    def link_to_blog_post(self, obj):
        link = urlresolvers.reverse("admin:blog_blogpost_change", args=[obj.blog_post.id])
        return u'<a href="%s">%s</a>' % (link, obj.blog_post)

    link_to_blog_post.allow_tags = True

admin.site.register(models.Comment, CommentAdmin)
