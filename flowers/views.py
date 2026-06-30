from django.db.models import Q
from django.db.models.functions import Lower
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from flowers.forms import ProductFilterForm, AddPageForm
from flowers.models import Flowers, Category
from flowers.utils import menu


def index(request):
    post = Flowers.objects.all()
    data = {'title': 'Главная страница',
            'posts': post,
            'menu': menu,
            'cat_select': 0,
            }
    return render(request, 'flowers/index.html', data)


def about(request):
    data = {'title': 'О сайте:',
            'menu': menu}
    return render(request, 'flowers/about.html', data)


def contacts(request):
    data = {'title': 'Контакты (обратная связь)',
            'menu': menu}
    return render(request, 'flowers/contacts.html', data)


def show_post(request, post_slug):
    post = get_object_or_404(Flowers, slug=post_slug)

    data = {
        'title': post.name,
        'menu': menu,
        'posts': post
    }

    return render(request, 'flowers/post.html', data)


def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Flowers.objects.filter(cat_id=category.pk)

    data = {
        'title': f'Рубрика: {category.name}',
        'menu': menu,
        'cat_select': category.id,
        'posts': posts
    }

    return render(request, 'flowers/category.html', data)


def flower_search(request):
    query = request.GET.get('query_text', '').strip().lower()
    all_flowers = Flowers.objects.select_related('cat').all()

    if query:
        results = []
        for flower in all_flowers:
            flower_name = flower.name.lower()
            # Проверяем, что категория существует
            category_name = flower.cat.name.lower() if flower.cat else ""

            # Если запрос есть в названии или в категории, добавляем в результаты
            if query in flower_name or query in category_name:
                results.append(flower)
    else:
        results = all_flowers

    data = {'title': 'Поиск:',
            'menu': menu,
            'results': results,
            'query': request.GET.get('query_text', '')}
    return render(request, 'flowers/search.html', data)


def add_page(request):
    if request.method == 'POST':
        form = AddPageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AddPageForm()

    data = {'title': 'Добавить статью',
            'menu': menu,
            'form': form}
    return render(request, 'flowers/add_page.html', data)
