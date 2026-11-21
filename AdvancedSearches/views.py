на всякий випадок:

env\Scripts\activate
python manage.py shell
from app.views import author_filter_advanced, author_order_by, author_in, author_startswith, author_bulk_create, author_values, author_first_last, author_exists, author_union

...

# ── РОЗШИРЕНІ ЗАПИТИ ──────────────────────────────────────────────────────────

def author_filter_advanced(request):
    """filter з різними умовами"""

    # lte / gte - менше або рівно / більше або рівно
    authors = Author.objects.filter(rating__gte=8.0)                  # rating >= 8.0
    authors = Author.objects.filter(rating__lte=5.0)                  # rating <= 5.0
    authors = Author.objects.filter(rating__gte=7.0, rating__lte=9.0) # 7.0 <= rating <= 9.0

    # lt / gt - строго менше / строго більше
    authors = Author.objects.filter(birth_year__gt=1800)              # birth_year > 1800
    authors = Author.objects.filter(birth_year__lt=1900)              # birth_year < 1900

    for author in authors:
        print(f'id={author.id}  name={author.name}  rating={author.rating}')


def author_order_by(request):
    """order_by - сортування"""

    authors = Author.objects.all().order_by('name')           # за іменем A...Z
    authors = Author.objects.all().order_by('-name')          # за іменем Z...A (мінус = DESC)
    authors = Author.objects.all().order_by('rating', 'name') # спочатку за рейтингом, потім за іменем

    for author in authors:
        print(f'name={author.name}  rating={author.rating}')


def author_in(request):
    """in - значення зі списку (аналог SQL IN)"""

    authors = Author.objects.filter(name__in=['Іван Франко', 'Леся Українка', 'Шевченко'])
    # SELECT * FROM authors WHERE name IN ('Іван Франко', 'Леся Українка', 'Шевченко')

    for author in authors:
        print(f'name={author.name}')


def author_startswith(request):
    """startswith / istartswith - починається з (i = case insensitive)"""

    authors = Author.objects.filter(name__startswith='Іван')  # чутливо до регістру
    authors = Author.objects.filter(name__istartswith='іван') # нечутливо до регістру

    # також є:
    # name__endswith  - закінчується на
    # name__contains  - містить підрядок
    # name__icontains - містить підрядок (нечутливо до регістру)

    for author in authors:
        print(f'name={author.name}')


def author_bulk_create(request):
    """bulk_create - вставка багатьох записів одним запитом (швидше ніж N окремих create)"""

    authors = [
        Author(name='Григорій Сковорода',   birth_year=1722, rating=8.5),
        Author(name='Панас Мирний',         birth_year=1849, rating=7.9),
        Author(name='Михайло Коцюбинський', birth_year=1864, rating=8.8),
    ]

    created = Author.objects.bulk_create(authors)
    # один INSERT з усіма рядками замість трьох окремих

    print(f'створено записів: {len(created)}')
    for author in created:
        print(f'name={author.name}')


def author_values(request):
    """values - повертає словники замість об'єктів моделі (менше пам'яті)"""

    # всі поля як словники
    authors = Author.objects.values()
    for author in authors:
        print(author)                    # {'id': 1, 'name': '...', 'birth_year': ..., 'rating': ...}

    # тільки вибрані поля
    authors = Author.objects.values('id', 'name')
    for author in authors:
        print(author)                    # {'id': 1, 'name': '...'}

    # values_list - повертає кортежі замість словників
    authors = Author.objects.values_list('id', 'name')
    for author in authors:
        print(author)                    # (1, 'Іван Франко')

    # values_list з flat=True - повертає плаский список (тільки для одного поля), плаский список - це просто список значень без кортежів
    names = Author.objects.values_list('name', flat=True)
    print(list(names))                   # ['Іван Франко', 'Леся Українка', ...]


def author_first_last(request):
    """first / last - перший і останній запис"""

    # повертає об'єкт або None якщо таблиця порожня
    first = Author.objects.all().first() # перший за поточним ordering (name)
    last  = Author.objects.all().last()  # останній

    first_by_rating = Author.objects.order_by('rating').first() # з найменшим рейтингом
    last_by_rating  = Author.objects.order_by('rating').last()  # з найбільшим рейтингом

    print(f'перший: {first}')
    print(f'останній: {last}')
    print(f'найнижчий рейтинг: {first_by_rating}')
    print(f'найвищий рейтинг: {last_by_rating}')


def author_exists(request):
    """exists - перевірка чи існує хоч один запис (швидше ніж count або all)"""

    # повертає True або False, не завантажує дані
    has_authors = Author.objects.exists()
    print(f'є хоч один автор: {has_authors}')

    franco_exists = Author.objects.filter(name='Іван Франко').exists()
    print(f'Іван Франко існує: {franco_exists}')

    # count - кількість записів
    total = Author.objects.count()
    print(f'всього авторів: {total}')


def author_union(request):
    """union - об'єднання двох QuerySet (аналог SQL UNION)"""

    # два окремі запити
    classic_authors = Author.objects.filter(birth_year__lt=1900) # народились до 1900
    modern_authors  = Author.objects.filter(rating__gte=9.0)     # або рейтинг 9.0+

    # union об'єднує результати і прибирає дублікати
    combined = classic_authors.union(modern_authors)

    # union(all=True) - зберігає дублікати (аналог UNION ALL)
    combined_with_duplicates = classic_authors.union(modern_authors, all=True)

    for author in combined:
        print(f'name={author.name}  birth_year={author.birth_year}  rating={author.rating}')

###############################################################################################

...