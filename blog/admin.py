from django import forms
from django.contrib import admin
from django.shortcuts import redirect

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


class BlogPostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        exclude = ['created_at']
        model = models.BlogPost


class BlogPostAdmin(DjangoObjectActions, admin.ModelAdmin):
    form = BlogPostForm
    filter_horizontal = ('categories', )
    inlines = (ContentImageInline, SourceCodeInline)

    def preview(self, request, obj):
        response = redirect('blog:blog_post_view', blog_post_id=obj.id)
        response['Location'] += '?preview_key={}'.format(obj.preview_key)
        return response

    change_actions = ('preview', )


admin.site.register(models.BlogPost, BlogPostAdmin)


class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Category, CategoryAdmin)
