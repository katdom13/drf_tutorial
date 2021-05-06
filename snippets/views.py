from django.contrib.auth.models import User
from rest_framework import generics, permissions

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
