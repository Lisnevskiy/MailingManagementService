from django.conf import settings
from django.core.cache import cache

from blog.models import Blog


def get_blogs_cache():
    if settings.CACHE_ENABLED:
        key = 'blog_list'
        blog_list = cache.get(key)

        if blog_list is None:
            blog_list = Blog.objects.order_by('-publication_date')[:3]
            cache.set(key, blog_list)

    else:
        blog_list = Blog.objects.order_by('-publication_date')[:3]

    return blog_list
