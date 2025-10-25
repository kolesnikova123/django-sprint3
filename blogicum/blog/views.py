from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from blog.models import Post

from .const import LIMIT


def index(request):
    """Главная страница проекта. Выводятся 5 последних публикаций."""
    template = 'blog/index.html'

    posts = Post.objects.filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    ).order_by('-pub_date')[:LIMIT]

    context = {'posts': posts}
    return render(request, template, context=context)


def post_detail(request, id):
    """Страница отдельной публикации."""
    template = 'blog/detail.html'

    post = get_object_or_404(
        Post,
        pk=id,
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    )

    context = {'post': post}
    return render(request, template, context=context)


def category_posts(request, category_slug):
    """Страница категории."""
    template = 'blog/category.html'

    posts = Post.objects.filter(
        category__slug=category_slug,
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True
    ).select_related('category').order_by('-pub_date')

    if not posts.exists():
        raise Http404('Ничего не нашлось!')

    context = {'posts': posts}
    return render(request, template, context=context)
