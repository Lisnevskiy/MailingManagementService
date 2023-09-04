from django.conf import settings
from django.core.cache import cache

from blog.models import Blog


def get_blogs_cache():
    """
    Получает список блогов из кэша или базы данных.
    Returns:
        QuerySet: Список трех последних блогов, либо None, если кэш отключен.
    """
    if settings.CACHE_ENABLED:
        key = 'blog_list'
        blog_list = cache.get(key)

        if blog_list is None:
            # Если блоги не найдены в кэше, получаем их из базы данных и кешируем
            blog_list = Blog.objects.order_by('-publication_date')[:3]
            cache.set(key, blog_list)
    else:
        # Если кэш отключен, получаем блоги напрямую из базы данных
        blog_list = Blog.objects.order_by('-publication_date')[:3]

    return blog_list
