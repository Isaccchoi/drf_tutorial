from rest_framework import serializers

from .models import Snippet


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        models = Snippet
        fields = (
            'id',
            'title',
            'code',
            'linenos',
            'language',
            'style',
        )
