from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Blog(models.Model):
    title = models.CharField(max_length=250, verbose_name='заголовок')
    content = models.TextField(verbose_name='содержание')
    image = models.ImageField(upload_to='blogs/', verbose_name='изображение')
    views_count = models.PositiveIntegerField(default=0, verbose_name='количество просмотров')
    publication_date = models.DateField(auto_now_add=True, verbose_name='дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
