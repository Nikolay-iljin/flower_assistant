from django.shortcuts import render

menu = [{'title': "Главная страница", 'url_name': 'index'},
        {'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Поиск", 'url_name': 'search'},
        # {'title': "Войти", 'url_name': 'login'}   переделали в шаблоне base.html
        ]

data_db = [{'id': 1, 'title': 'Крапива', 'content': 'Какая то информация об этом цветке - '},
           {'id': 2, 'title': 'Борщевик', 'content': 'Какая то информация об этом цветке - '},
           {'id': 3, 'title': 'Кактус', 'content': 'Какая то информация об этом цветке - '}]


def index(request):
    # post = Flowers.objects.all()
    post = data_db
    data = {'title': 'Главная страница',
            'posts': post,
            'menu': menu,
            'cat_select': 0,
            }
    return render(request, 'flowers/index.html', data)


def about(request):
    data = {'title': 'О нас',
            'menu': menu,
            'posts': data_db}
    return render(request, 'flowers/about.html', data)


def add_page(request):
    data = {'title': 'Добавить страницу',
            'menu': menu,
            'posts': data_db}
    return render(request, 'flowers/about.html', data)


def contacts(request):
    data = {'title': 'Контакты (обратная связь)',
            'menu': menu,
            'posts': data_db}
    return render(request, 'flowers/contacts.html', data)