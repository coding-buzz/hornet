from django.conf.urls import url
from django.contrib.auth.decorators import login_required

import pinger.views as views


urlpatterns = [
    url(r'^$', login_required(views.DashboardView.as_view()), name='dashboard'),
]
