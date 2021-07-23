import django_filters

from main.models import Post


class PostFilter(django_filters.FilterSet):
    class Meta:
        model = Post
        fields = ['title', 'description']
