from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.db.models import Avg, Count, Sum, Max, Min, F, Q
from app.models import Author, Book


# =============================================================================
# CRUD ДЛЯ AUTHOR (це було вже :)
# =============================================================================

# ── CREATE ────────────────────────────────────────────────────────────────────
def author_create_method1(request):
    """Вставка автора через objects.create()"""
    author = Author.objects.create(
        name='Іван Франко',
        birth_year=1856,
        rating=9.2
    )
    print(f"Створено: {author} (id={author.id})")


def author_create_method2(request):
    """Вставка через save()"""
    author = Author()
    author.name = 'Леся Українка'
    author.birth_year = 1871
    author.rating = 9.5
    author.save()
    print(f"Створено: {author} (id={author.id})")


# ── READ ──────────────────────────────────────────────────────────────────────
def author_select_all(request):
    """Вибірка всіх авторів"""
    authors = Author.objects.all()
    for a in authors:
        print(f'id={a.id}  name={a.name}  birth_year={a.birth_year}  rating={a.rating}')


def author_select_by_condition(request):
    """filter + get"""
    # filter - багато записів
    authors = Author.objects.filter(rating__gte=9.0)
    for a in authors:
        print(f'filter rating >=9: {a.name}')

    # get - один запис
    try:
        author = Author.objects.get(name='Іван Франко')
        print(f'get: {author}')
    except (Author.DoesNotExist, Author.MultipleObjectsReturned) as e:
        print(f'Помилка: {e}')


# ── UPDATE ────────────────────────────────────────────────────────────────────
def author_update(request):
    """Оновлення автора"""
    try:
        author = Author.objects.get(name='Іван Франко')
        print(f'До: rating={author.rating}')
        author.rating = 9.9
        author.save()
        print(f'Після: rating={author.rating}')
    except Author.DoesNotExist:
        print('Автора не знайдено')


# ── DELETE ────────────────────────────────────────────────────────────────────
def author_delete(request):
    """Видалення автора"""
    try:
        author = Author.objects.get(name='Леся Українка')
        author.delete()
        print(f'Видалено: {author.name}')
    except Author.DoesNotExist:
        print('Автора не знайдено')


# =============================================================================
# CRUD ДЛЯ BOOK + 1-M ЗАПИТИ
# =============================================================================

# ── CREATE Book ───────────────────────────────────────────────────────────────
def book_create(request):
    """Створення книги (з ForeignKey)"""
    try:
        author = Author.objects.get(name='Іван Франко')
        book = Book.objects.create(
            title='Каменярі',
            author=author, # ForeignKey - передаємо об'єкт автора
            pages=120,
            price=250.00,
            discount_price=199.50,
            published_year=1878,
            stock=15
        )
        print(f'Створено книгу: {book.title} автора {book.author.name}')
    except Author.DoesNotExist:
        print('Автор не знайдений')


# ── READ Books ────────────────────────────────────────────────────────────────
def book_select_all(request):
    """Всі книги"""
    books = Book.objects.all()
    for b in books:
        print(f'{b.title} - {b.author.name} ({b.published_year}), ціна: {b.price}') # b.author.name - доступ до поля name через ForeignKey author


def book_select_with_author(request):
    """1-M: книги з автором (select_related - один JOIN)"""
    books = Book.objects.select_related('author').all() # select_related виконує JOIN і отримує дані автора разом з книгою, що зменшує кількість запитів до бази даних
    for b in books:
        print(f'{b.title} - {b.author.name} (рейтинг автора: {b.author.rating})')


def books_by_author(request):
    """1-M: всі книги конкретного автора (через related_name за замовчуванням book_set)"""
    try:
        author = Author.objects.get(name='Іван Франко')
        books = author.book_set.all() # або Book.objects.filter(author=author)
        for b in books: # author.book_set - доступ до книг автора через зворотній зв'язок ForeignKey (related_name за замовчуванням це назва моделі в нижньому регістрі + _set)
            print(f'Книга автора {author.name}: {b.title}')
    except Author.DoesNotExist:
        print('Автор не знайдений')


def books_advanced_filter(request):
    """Фільтри по автору + інші умови"""
    # книги авторів з рейтингом >= 8.5 і ціна зі знижкою
    books = Book.objects.filter(
        author__rating__gte=8.5, # фільтр по полю rating моделі Author через ForeignKey (дві підкреслення означають перехід до пов'язаного поля)
        discount_price__lt=F('price')
    ).select_related('author')

    for b in books:
        print(f'{b.title} ({b.author.name}) - знижка: {b.discount_price}')


# ── UPDATE Book ───────────────────────────────────────────────────────────────
def book_update(request):
    """Оновлення книги"""
    try:
        book = Book.objects.get(title='Каменярі')
        book.price = 280.00
        book.stock = 20
        book.save()
        print(f'Оновлено: {book.title}, нова ціна {book.price}')
    except Book.DoesNotExist:
        print('Книгу не знайдено')


# ── DELETE Book ───────────────────────────────────────────────────────────────
def book_delete(request):
    """Видалення книги"""
    try:
        book = Book.objects.get(title='Каменярі')
        book.delete()
        print(f'Видалено книгу: {book.title}')
    except Book.DoesNotExist:
        print('Книгу не знайдено')


# =============================================================================
# ФУНКЦІЇ АГРЕГУВАННЯ
# =============================================================================

def aggregation_examples(request):
    """Приклади aggregate() та annotate()"""

    # 1. aggregate() - одна цифра на весь QuerySet
    stats = Book.objects.aggregate(
        total_books=Count('id'),
        total_stock=Sum('stock'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price'),
        avg_rating=Avg('author__rating') # через ForeignKey
    )
    print("Загальна статистика книг:", stats)

    # 2. annotate() - додає поле до кожного об'єкта
    authors_with_books = Author.objects.annotate( # annotate додає до кожного автора нове поле, яке є результатом агрегування його книг
        num_books=Count('book'), # кількість книг у автора
        total_pages=Sum('book__pages'),
        avg_book_price=Avg('book__price')
    ).order_by('-num_books')

    for a in authors_with_books:
        print(f'{a.name}: {a.num_books} книг, '
              f'середня ціна {a.avg_book_price}, '
              f'всього сторінок {a.total_pages}')

    # 3. книги з кількістю... (наприклад, тільки автори з 1+ книгою)
    popular_authors = Author.objects.annotate(
        num_books=Count('book')
    ).filter(num_books__gte=2)

    print("Автори з 2+ книгами:")
    for a in popular_authors:
        print(f'{a.name} - {a.num_books} книг')


# =============================================================================
# СИРІ SQL ЗАПИТИ (raw) - на той випадок, якщо ORM не може виконати складний запит або потрібна оптимізація
# ну, або ви просто хочете написати SQL самі :) !але будьте обережні з безпекою (SQL injection) і сумісністю між базами даних!
# =============================================================================

def raw_sql_examples(request):
    """Приклади сирих запитів"""

    # 1. простий SELECT всіх авторів
    authors = Author.objects.raw("SELECT * FROM authors")
    for a in authors:
        print(f'RAW author: {a.name}')

    # 2. JOIN авторів і книг + агрегати
    sql = """
        SELECT a.id, a.name, COUNT(b.id) as book_count, AVG(b.price) as avg_price
        FROM authors a
        LEFT JOIN books b ON a.id = b.author_id
        GROUP BY a.id, a.name
        HAVING COUNT(b.id) > 0
        ORDER BY book_count DESC
    """
    results = Author.objects.raw(sql)
    for row in results:
        print(f'{row.name}: {row.book_count} книг, середня ціна ~ {row.avg_price}')

    # 3. вставка через raw (не рекомендується в продакшені!)
    # Author.objects.raw("INSERT INTO authors (name, birth_year, rating) VALUES (%s, %s, %s)", 
    #                    ['Тарас Шевченко', 1814, 9.8])

    # 4. оновлення через extra / raw (краще використовувати ORM)
    Book.objects.raw("""
        UPDATE books 
        SET discount_price = price * 0.8 
        WHERE discount_price IS NULL AND price IS NOT NULL
    """)


# =============================================================================
# ДОПОМІЖНІ ФУНКЦІЇ
# =============================================================================

def author_filter_advanced(request):
    """Розширені фільтри для Author"""
    authors = Author.objects.filter(
        Q(rating__gte=8.0) | Q(birth_year__lt=1800)
    ).exclude(rating=10.0)
    for a in authors:
        print(a)


def author_bulk_create(request):
    """Масова вставка"""
    authors = [
        Author(name='Григорій Сковорода', birth_year=1722, rating=8.5),
        Author(name='Панас Мирний', birth_year=1849, rating=7.9),
    ]
    Author.objects.bulk_create(authors)
    print(f'Створено {len(authors)} авторів')

##############################################################################################
# ТЕСТИ для python manage.py shell

from app.views import (
    author_create_method1, author_create_method2, author_select_all,
    author_select_by_condition, author_update, author_delete,
    book_create, book_select_all, book_select_with_author,
    books_by_author, books_advanced_filter, book_update, book_delete,
    aggregation_examples, raw_sql_examples,
    author_filter_advanced, author_bulk_create
)
  
# # =============================================================================
# # CRUD для Book + 1-M зв'язки
# # =============================================================================
# book_create(None)            
# book_select_all(None)
# book_select_with_author(None)
# books_by_author(None)
# books_advanced_filter(None)

# book_update(None)
# book_select_all(None)
# book_delete(None)
# book_select_all(None)

# # =============================================================================
# # Агрегація та анотація
# # =============================================================================
# aggregation_examples(None)

# # =============================================================================
# # Сирі SQL запити
# # =============================================================================
# raw_sql_examples(None)

##############################################################################################
# =============================================================================
# СТАРІ СТОРІНКИ (home, contact, about)
# =============================================================================

def home(request):
    assert isinstance(request, HttpRequest)
    return render(request, 'app/index.html', {
        'title': 'Home Page',
        'year': datetime.now().year,
    })


def contact(request):
    assert isinstance(request, HttpRequest)
    return render(request, 'app/contact.html', {
        'title': 'Contact',
        'message': 'Your contact page.',
        'year': datetime.now().year,
    })


def about(request):
    assert isinstance(request, HttpRequest)
    return render(request, 'app/about.html', {
        'title': 'About',
        'message': 'Your application description page.',
        'year': datetime.now().year,
    })