from django.conf.urls import url

import pinger.views as views


urlpatterns = [
    url(r'^$', views.DashboardView.as_view(), name='dashboard'),
]
