from django.views.generic import DetailView

from blog.models import Blog


class BlogDetailView(DetailView):
    model = Blog
    extra_context = {'title': 'Рассылка'}

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object
