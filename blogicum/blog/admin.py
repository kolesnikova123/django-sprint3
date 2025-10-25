from django.contrib import admin

from .models import Category, Location, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Представление для модели Category."""

    list_display = ['title', 'description',
                    'slug', 'is_published', 'created_at']
    search_fields = ['title', 'description', 'slug']
    list_filter = ['title', 'slug', 'is_published', 'created_at']


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    """Представление для модели Location."""

    list_display = ['name', 'is_published', 'created_at']
    search_fields = ['name']
    list_filter = ['name', 'is_published', 'created_at']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Представление для модели Post."""

    list_display = ['title', 'pub_date', 'author',
                    'location', 'category', 'is_published', 'created_at']
    search_fields = ['title', 'text', 'author', 'location', 'category']
    list_filter = ['pub_date', 'author',
                   'location', 'category', 'is_published', 'created_at']
