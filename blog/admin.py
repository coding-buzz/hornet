from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget

import models


class BlogPostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        exclude = ['created_at']
        model = models.BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    form = BlogPostForm
    filter_horizontal = ('categories', )


admin.site.register(models.BlogPost, BlogPostAdmin)


class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Category, CategoryAdmin)
