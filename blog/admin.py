from django.contrib import admin

import models


class BlogPostAdmin(admin.ModelAdmin):
    filter_horizontal = ('categories', )

admin.site.register(models.BlogPost, BlogPostAdmin)


class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Category, CategoryAdmin)
