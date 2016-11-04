from django.conf.urls import url

import blog.views as views


urlpatterns = [
    url(r'^$', views.index_view, name='index'),
    url(r'^posts/(?P<blog_post_id>\d+)/', views.blog_post_view, name='blog_post_view')
]
