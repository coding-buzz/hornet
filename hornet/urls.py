from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static

import views


urlpatterns = [
    url(r'^$', views.home, name='index'),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
