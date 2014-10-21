from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('rest.views',
    url(r'^requests/$', 'request_list'),
    url(r'^request/(?P<pk>[0-9]+)$', 'request_detail'),
)

urlpatterns = format_suffix_patterns(urlpatterns)
