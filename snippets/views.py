from django.contrib.auth.models import User
from rest_framework import generics, permissions, renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Snippet
from .permissions import IsOwnerOrReadOnly
from .serializers import SnippetSerializer, UserSerializer


class SnippetListView(generics.ListCreateAPIView):
    """
    List all snippets, or create a new snippet
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    # Ensure that authenticated requests get read-write access,
    # and unauthenticated requests get read-only access
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    """
    Associate the snippet and the user who created the snippet
    by modifying how the instance is saved
    """
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a code snippet
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    # Ensure that authenticated requests get read-write access,
    # and unauthenticated requests get read-only access
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]


class UserListView(generics.ListAPIView):
    """
    Read-only list view for the user representation
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    """
    Read-only detail view for a user
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(["GET"])
def api_root(request, format=None):
    # We're using REST framework's reverse function in order to return fully-qualified URLs
    # URL patterns are identified by convenience names declared in snippets/urls.py
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format),
    })



class SnipperHighlightView(generics.GenericAPIView):
    """
    HTML endpoint for highlighted snippets
    """
    queryset = Snippet.objects.all()

    # Render pre-rendered HTML
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        """
        Custom get method that returns an object ATTRIBUTE
        """
        snippet = self.get_object()
        return Response(snippet.highlighted)
