from django.contrib.auth.models import User
from rest_framework import permissions, renderers, viewsets
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Snippet
from .permissions import IsOwnerOrReadOnly
from .serializers import SnippetSerializer, UserSerializer


# We use the ModelViewSet class in order to get the
# complete set of default read and write operations.
class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve',
    'update', and 'destroy' actions

    Additionally, we also provide an extra 'highlight' action
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    # Ensure that authenticated requests get read-write access,
    # and unauthenticated requests get read-only access
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    # This decorator can be used to add any custom endpoints
    # that don't fit into the standard create/update/delete style
    # custom actions which use the @action decorator will respond to GET requests by default
    # We can use the methods argument if we wanted an action that responded to POST requests
    # The URLs for custom actions by default depend on the method name itself
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        """
        Custom action method that returns an object ATTRIBUTE
        """
        snippet = self.get_object()
        return Response(snippet.highlighted)

    """
    Associate the snippet and the user who created the snippet
    by modifying how the instance is saved
    """
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides 'list' and 'retrieve' actions
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
