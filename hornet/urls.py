from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static

import views
import pinger.urls

urlpatterns = [
    url(r'^$', views.home, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^pinger/', include(pinger.urls, namespace='pinger')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
