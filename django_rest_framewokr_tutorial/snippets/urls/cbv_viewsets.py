from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from ..views.cbv_viewsets import SnippetViewSet

snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create',
})
snippet_detail = SnippetViewSet.as_view({
    'get': 'retreive',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

urlpatterns = [
    url(r'^$', snippet_list, name='snippet_list'),
    url(r'^(?P<pk>\d+)/$', snippet_detail, name='snippet_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
