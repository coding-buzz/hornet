from django.conf.urls import url

import blog.views as views


urlpatterns = [
    url(r'^$', views.index_view, name='index'),
    url(r'^category/(?P<category_name>.+)/', views.category_view, name='category_view'),
    url(r'^posts/(?P<blog_post_id>\d+)/notification', views.notification_preview, name='notification_preview'),
    url(r'^posts/(?P<blog_post_id>\d+)/add_comment', views.add_comment, name='add_comment'),
    url(r'^posts/(?P<blog_post_id>\d+)/', views.blog_post_view, name='blog_post_view')
]
