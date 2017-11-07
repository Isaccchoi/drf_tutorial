from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from ..views import fbv

urlpatterns = [
    url(r'^$', fbv.snippet_list, name='snippet_list'),
    url(r'^(?P<pk>\d+)/$', fbv.snippet_detail, name='snippet_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
