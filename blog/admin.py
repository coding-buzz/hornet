from django.contrib import admin

import models


class BlogPostAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.BlogPost, BlogPostAdmin)
