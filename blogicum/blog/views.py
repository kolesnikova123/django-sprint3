from django.db.models import Q
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from blog.models import Post


def index(request):
    """Главная страница проекта. Выводятся 5 последних публикаций."""
    template = 'blog/index.html'

    posts = Post.objects.filter(
        Q(pub_date__lte=timezone.now())
        & Q(is_published=True)
        & Q(category__is_published=True)
    ).order_by('-pub_date')[0:5]

    context = {'posts': posts}
    return render(request, template, context=context)


def post_detail(request, id):
    """Страница отдельной публикации."""
    template = 'blog/detail.html'

    post = get_object_or_404(Post, pk=id, )

    if (post.pub_date > timezone.now()
            or not post.is_published
            or not post.category.is_published):
        raise Http404('Ничего не нашлось!')

    context = {'post': post}
    return render(request, template, context=context)


def category_posts(request, category_slug):
    """Страница категории."""
    template = 'blog/category.html'

    posts = Post.objects.filter(
        Q(category__slug=category_slug)
        & Q(is_published=True)
        & Q(pub_date__lte=timezone.now())
        & Q(category__is_published=True)
    ).select_related('category').order_by('-pub_date')

    if not posts.exists():
        raise Http404('Ничего не нашлось!')

    context = {'posts': posts}
    return render(request, template, context=context)
