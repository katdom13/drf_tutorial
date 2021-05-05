from rest_framework import serializers

from .models import LANGUAGE_CHOICES, STYLE_CHOICES, Snippet


class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    line_nos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):
        """
        Create and return a new 'Snippet' instance, given the validated data
        """
        return Snippet.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """
        Update and return an existing 'Snippet' instance, given the validated data
        """
        instance.title = validated_data('title', instance.title)
        instance.code = validated_data('code', instance.code)
        instance.line_nos = validated_data('line_nos', instance.line_nos)
        instance.language = validated_data('language', instance.language)
        instance.style = validated_data('style', instance.style)

        instance.save()
        return instance

