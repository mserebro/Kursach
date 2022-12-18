from django.db import models
from django.urls import reverse


class Liblinks(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    authors = models.CharField(max_length=150, blank=True, default="AUTHOR", verbose_name="Авторы")
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    # updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    # is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    # category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
    views = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'
        ordering = ['created_at']
