from django.core.cache import cache

from main.models import Post


def post_all():
    # return Post.objects.all()
    key = Post().__class__.cache_key()
    # breakpoint()
    if key in cache:
        all = cache.get(key)
    else:
        all = Post.objects.all()
        cache.set(key, all, 86400)

    return all


def post_find(post_id: int) -> Post:
    return Post.objects.get(id=post_id)
