from django.conf.urls import url

import blog.views as views


urlpatterns = [
    url(r'^$', views.index_view, name='index'),
]
