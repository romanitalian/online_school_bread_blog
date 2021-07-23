from rest_framework import serializers

from main.models import Rate, Post


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = (
            'id',
            'currency',
            'source',
            'buy',
            'sale',
            'created',
            'get_source_display',
        )


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'description',
            'content',
        )
