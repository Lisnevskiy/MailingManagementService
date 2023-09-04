from django.views.generic import DetailView

from blog.models import Blog


class BlogDetailView(DetailView):
    """
    Представление для отображения деталей блога.
    """
    model = Blog
    extra_context = {'title': 'Рассылка'}

    def get_object(self, queryset=None):
        """
        Получает объект блога и увеличивает счетчик просмотров на 1.
        Args:
            queryset (QuerySet, optional): Набор данных для получения объекта. Defaults to None.
        Returns:
            Blog: Объект блога.
        """
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object
