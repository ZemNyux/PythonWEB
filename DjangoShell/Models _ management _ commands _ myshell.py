from django.core.management.base import BaseCommand
from django.apps import apps
from app.models import Author, Book 

class Command(BaseCommand):
    help = 'Наповнює базу даних початковими авторами та книгами'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Ласкаво просимо в кастомний шелл!'))
        
        # ініціалізація моделей (за потреби)
        apps.get_models()

        # створення першого автора та його книги
        author1 = Author.objects.create(
            name='Тарас Григорович Шевченко',
            birth_year=1814,
            rating=9.5
        )

        Book.objects.create(
            title='Кобзар',
            author=author1,
            pages=325,
            price=150.00,
            published_year=1840,
            stock=10
        )

        # створення другого автора та його книги
        author2 = Author.objects.create(
            name='Леся Українка',
            birth_year=1871,
            rating=9.6
        )

        Book.objects.create(
            title='Лісова пісня',
            author=author2,
            pages=123,
            price=250.00,
            published_year=1912,
            stock=20
        )

        self.stdout.write(self.style.SUCCESS('\nАвтори та книги створені успішно!\n'))

        # вивід результатів у консоль
        print('Всі автори:')
        print(Author.objects.all())                
        
        print('\nАвтори як словники:')
        print(list(Author.objects.values()))                
        
        print('\nВсі книжки:')
        print(Book.objects.all())                
        
        print('\nВсі книжки як словники:')
        print(list(Book.objects.values()))