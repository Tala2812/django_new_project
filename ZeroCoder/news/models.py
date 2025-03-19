from django.db import models
from django.contrib.auth.models import User  # Импортируем модель User

class NewsPost(models.Model):  # Изменил имя класса на PEP8-совместимое
    title = models.CharField('Название новости', max_length=50)
    short_description = models.CharField('Краткое описание новости', max_length=200)
    text = models.TextField('Новость')
    pub_date = models.DateTimeField('Дата публикации')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор новости')  # Добавляем поле для пользователя

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
    def __str__(self):
        return self.title


