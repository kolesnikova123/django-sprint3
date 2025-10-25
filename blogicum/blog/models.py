from django.contrib.auth import get_user_model
from django.db import models

from .const import MAX_LENGTH


# Пользователь (эту модель описывать не нужно, она встроена в Django).
User = get_user_model()


class CommonInfo(models.Model):
    """Абстрактный базовый класс для общих полей других моделей."""

    is_published = models.BooleanField(
        'Опубликовано', default=True,
        help_text='Снимите галочку, чтобы скрыть публикацию.'
    )
    created_at = models.DateTimeField('Добавлено', auto_now_add=True)

    class Meta:
        """Класс Meta этой модели."""

        abstract = True


class Category(CommonInfo):
    """Тематическая категория."""

    title = models.CharField('Заголовок', max_length=MAX_LENGTH)
    description = models.TextField('Описание')
    slug = models.SlugField(
        'Идентификатор', unique=True,
        help_text=('Идентификатор страницы для URL; разрешены символы '
                   'латиницы, цифры, дефис и подчёркивание.'
                   )
    )

    class Meta:
        """Класс Meta этой модели."""

        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        """Метод приведения к строке."""
        return self.title


class Location(CommonInfo):
    """Географическая метка."""

    name = models.CharField('Название места', max_length=MAX_LENGTH)

    class Meta:
        """Класс Meta этой модели."""

        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        """Метод приведения к строке."""
        return self.name


class Post(CommonInfo):
    """Публикация."""

    title = models.CharField('Заголовок', max_length=MAX_LENGTH)
    text = models.TextField('Текст')
    pub_date = models.DateTimeField(
        'Дата и время публикации',
        help_text=('Если установить дату и время в будущем — '
                   'можно делать отложенные публикации.'
                   )
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name='Автор публикации',
        related_name='author_posts'
    )
    location = models.ForeignKey(
        Location, on_delete=models.SET_NULL, null=True,
        verbose_name='Местоположение',
        related_name='location_posts'
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True,
        verbose_name='Категория',
        related_name='category_posts'
    )

    class Meta:
        """Класс Meta этой модели."""

        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        """Метод приведения к строке."""
        return self.title
