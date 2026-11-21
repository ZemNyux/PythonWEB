from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from app.models import Author


# ── CREATE ────────────────────────────────────────────────────────────────────

def author_create_method1(request):
    """Вставка автора через objects.create() - один рядок, одразу зберігає в БД"""
    author = Author.objects.create(
        name='Іван Франко',
        birth_year=1856,
        rating=9.2
    )
    print(author)      # Іван Франко
    print(author.id)   # id призначений базою
    print(author.name) # Іван Франко


def author_create_method2(request):
    """Вставка автора через save() - спочатку створює об'єкт в пам'яті, потім зберігає"""
    author = Author()
    author.name = 'Леся Українка'
    author.birth_year = 1871
    author.rating = 9.5
    author.save()    # тільки тут уже INSERT в базу
    print(author)    # Леся Українка
    print(author.id) # id призначений базою


# ── READ ──────────────────────────────────────────────────────────────────────

def author_select_all(request):
    """Вибірка всіх авторів"""
    authors = Author.objects.all()
    for author in authors:
        print(f'id={author.id}  name={author.name}  birth_year={author.birth_year}  rating={author.rating}')


def author_select_by_condition(request):
    """Вибірка автора по умові - filter повертає QuerySet, get повертає один об'єкт"""
    # filter - повертає список (може бути 0, 1 або багато записів)
    authors = Author.objects.filter(name='Іван Франко')
    for author in authors:
        print(f'filter -> id={author.id}  name={author.name}')

    # get - повертає рівно один запис, кидає виняток якщо не знайдено або знайдено більше одного
    try:
        author = Author.objects.get(name='Леся Українка')
        print(f'get -> id={author.id}  name={author.name}')
    except Author.DoesNotExist:
        print('Автора не знайдено')
    except Author.MultipleObjectsReturned:
        print('Знайдено більше одного автора')


# ── UPDATE ────────────────────────────────────────────────────────────────────

def author_update(request):
    """Оновлення автора - спочатку отримуємо запис, потім змінюємо і зберігаємо"""
    try:
        author = Author.objects.get(name='Іван Франко')
        print(f'до оновлення: rating={author.rating}')

        author.rating = 9.9
        author.save() # UPDATE в базі тільки тут

        print(f'після оновлення: rating={author.rating}')
    except Author.DoesNotExist:
        print('Автора не знайдено')


# ── DELETE ────────────────────────────────────────────────────────────────────

def author_delete(request):
    """Видалення автора"""
    try:
        author = Author.objects.get(name='Леся Українка')
        print(f'видаляємо: {author.name}')

        author.delete() # DELETE в базі

        print('автора видалено')
    except Author.DoesNotExist:
        print('Автора не знайдено')


################################################################################
# тести в python manage.py shell:

# from app.views import author_create_method1, author_create_method2
# from app.views import author_select_all, author_select_by_condition
# from app.views import author_update, author_delete
# author_create_method1(None)
# author_create_method2(None)
# author_select_all(None)
# author_select_by_condition(None)
# author_update(None)
# author_select_all(None)  
# author_delete(None)
# author_select_all(None)
################################################################################

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title': 'Home Page',
            'year': datetime.now().year,
        }
    )


def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title': 'Contact',
            'message': 'Your contact page.',
            'year': datetime.now().year,
        }
    )


def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title': 'About',
            'message': 'Your application description page.',
            'year': datetime.now().year,
        }
    )