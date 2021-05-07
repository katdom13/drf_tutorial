from django.contrib.auth.models import User
from rest_framework import serializers

from .models import LANGUAGE_CHOICES, STYLE_CHOICES, Snippet


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    # The source argument controls which attribute is used to populate a field,
    # and can point at any attribute on the serialized instance
    owner = serializers.ReadOnlyField(source='owner.username')

    # This field is of the same type as the 'url' field,
    # except it points to 'snippet-highlight' url pattern, instead of 'snippet-detail'
    # We also need to indicate that any format suffixed hyperlinks
    # it returns should use the '.html' suffix
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ['url', 'id', 'highlight', 'title', 'code', 'line_nos', 'language', 'style', 'owner']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']
