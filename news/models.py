from distutils.command.upload import upload
from django.urls import reverse
from django.db import models


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)   

    def get_absolute_url(self):
        return reverse("view_news", kwargs={"pk": self.pk})

    def __str__(self):
        return f'({self.pk}) {self.title}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['created_at']

class Category(models.Model):
    title=models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории') #  Сделали индексацию
    
    def get_absolute_url(self):
        return reverse("category", kwargs={"category_id": self.pk})

    def __str__(self):
        return f'{self.title}'
    class Meta:
        verbose_name='Категория'
        verbose_name_plural='Категории'
        ordering=['title']