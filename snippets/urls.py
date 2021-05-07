from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views

urlpatterns = [
    path('', views.api_root),
    path('snippets/', views.SnippetListView.as_view(), name='snippet-list'),
    path('snippets/<int:pk>/', views.SnippetDetailView.as_view(), name='snippet-detail'),
    path('snippets/<int:pk>/highlight/', views.SnipperHighlightView.as_view(), name='snippet-highlight'),
    path('users/', views.UserListView.as_view(), name='user-list'),
    path('users/<int:pk>', views.UserDetailView.as_view(), name='user-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
