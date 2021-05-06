from rest_framework import generics

from .models import Snippet
from .serializers import SnippetSerializer


class SnippetListView(generics.ListCreateAPIView):
    """
    List all snippets, or create a new snippet
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a code snippet
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
