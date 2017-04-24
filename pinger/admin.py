from django.contrib import admin

import pinger.models as models


admin.site.register(models.PingCheck)
admin.site.register(models.ResponseCheck)
