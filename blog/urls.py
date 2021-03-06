from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new/$', views.post_new, name='post_new'),
    #url(r'^index.xml$', views.index_xml, name='index_xml'),
    url(r'^(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^(?P<post_pk>\d+)/comments/new/$', views.comment_new, name='comment_new'),
    url(r'^(?P<post_pk>\d+)/comments/(?P<pk>\d+)/edit/$', views.comment_edit, name='comment_edit'),
    url(r'^(?P<name>[a-zA-Z]+)/$', views.post_detail, name='post_detail'),
    url(r'^(?P<year>\d{4})/$', views.list_by_day, name='list_by_day'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/$', views.list_by_day, name='list_by_day'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$', views.list_by_day, name='list_by_day'),
]