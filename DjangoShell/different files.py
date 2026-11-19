.\env\Scripts\activate

pip install mssql-django

========================================================================================================
settings.py:

...
DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': 'test',
        'HOST': 'localhost',
        'OPTIONS': {
            'driver': 'ODBC Driver 18 for SQL Server',
            'trusted_connection': 'yes',
            'extra_params': 'TrustServerCertificate=yes;',
        },
    }}
...

========================================================================================================
models.py:

from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)
    birth_year = models.IntegerField(default=1960)
    rating = models.FloatField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    pages = models.IntegerField(default=100)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=100)
    published_year = models.IntegerField(default=2026)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.title


========================================================================================================
python manage.py makemigrations
python manage.py migrate
========================================================================================================
python manage.py shell (набрати цю команду в Developer PowerShell)

from django.apps import apps

apps.get_models()

from app.models import Author, Book 

# ── ДОДАВАННЯ ─────────────────────────────────────────────────────────────────

author = Author.objects.create(
    name='Шевченко',
    birth_year=1814,
    rating=9.5
)

book = Book.objects.create(
    title='Кобзар',
    author=author,
    pages=325,
    price=150.00,
    published_year=1840,
    stock=10
)

# ── ПЕРЕГЛЯД ──────────────────────────────────────────────────────────────────

Author.objects.all()                          # всі автори
Author.objects.values()                       # як словники
Author.objects.filter(rating__gte=7)          # з рейтингом 7+
Author.objects.get(name='Шевченко')           # один конкретний (кидає виняток якщо не знайдено)

Book.objects.all()
Book.objects.select_related('author').all()   # з підтягуванням автора (JOIN, без N+1)
Book.objects.filter(author__name='Шевченко')  # книги конкретного автора

# ── ОНОВЛЕННЯ ─────────────────────────────────────────────────────────────────

# один запис
author = Author.objects.get(name='Шевченко')
author.rating = 10.0
author.save()

# або одразу без fetch (один SQL UPDATE)
Author.objects.filter(name='Шевченко').update(rating=10.0)

# ── ВИДАЛЕННЯ ─────────────────────────────────────────────────────────────────

# один запис
author = Author.objects.get(name='Шевченко')
author.delete() # видалить і всі його книги (CASCADE)

# або одразу
Author.objects.filter(birth_year__lt=1800).delete()
