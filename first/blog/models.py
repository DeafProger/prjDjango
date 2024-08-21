from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    slug = models.CharField(max_length=150, verbose_name='slug', blank=True, null=True)
    content = models.TextField(verbose_name='Содержимое')
    picture = models.ImageField(upload_to='blog', verbose_name='Изображение', blank=True, null=True)
    created_at = models.DateField(auto_now=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Опубликованно')
    views_count = models.IntegerField(default=0, verbose_name='Просмотры')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ('title', 'content')
