from django.urls import path
from rest_framework import renderers
from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views

# We bind our ViewSet classes into a set of concrete views
# We create multiple views from each ViewSet class,
# by binding the http methods to the required action for each view
snippet_list = views.SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
snippet_detail = views.SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
snippet_highlight = views.SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = views.UserViewSet.as_view({
    'get': 'list'
})
user_detail = views.UserViewSet.as_view({
    'get': 'retrieve'
})

# Register the views with the URL conf as usual
urlpatterns = [
    path('', views.api_root),
    path('snippets/', snippet_list, name='snippet-list'),
    path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
    path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>', user_detail, name='user-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
