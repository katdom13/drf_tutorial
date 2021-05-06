from rest_framework import generics, mixins

from .models import Snippet
from .serializers import SnippetSerializer

"""
The base class provides the core functionality,
and the mixin classes provide the .list() and .create() actions
"""

class SnippetListView(mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView):
    """
    List all snippets, or create a new snippet
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class SnippetDetailView(mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):
    """
    Retrieve, update, or delete a code snippet
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
