from django.conf.urls import patterns, url
from cms import views

urlpatterns = patterns('',
    url(r'^$', views.homepage, name = 'homepage'),
    url(r'^new_page/$', views.new_post, name = 'new_page'),
    url(r'^page/(?P<blog_post_slug>[\w\-]+)/$', views.view_post, name = 'view_post'),
    url(r'^archive/$', views.archive, name = 'archive'),
    )