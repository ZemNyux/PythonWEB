from datetime import date

from django.db import migrations


def seed_core(apps, schema_editor):
    CompanyStat = apps.get_model('core', 'CompanyStat')
    ServiceDirection = apps.get_model('core', 'ServiceDirection')
    CompanyPrinciple = apps.get_model('core', 'CompanyPrinciple')
    NewsArticle = apps.get_model('core', 'NewsArticle')
    TeamMember = apps.get_model('core', 'TeamMember')
    ContactOffice = apps.get_model('core', 'ContactOffice')
    ContactLocation = apps.get_model('core', 'ContactLocation')

    if not CompanyStat.objects.exists():
        CompanyStat.objects.bulk_create([
            CompanyStat(value='12+', label='Років на ринку', sort_order=1),
            CompanyStat(value='4', label='Міжнародні філії', sort_order=2),
            CompanyStat(value='180+', label='Реалізованих проєктів', sort_order=3),
            CompanyStat(value='99.9%', label='Безвідмовність систем', sort_order=4),
        ])

    if not ServiceDirection.objects.exists():
        ServiceDirection.objects.bulk_create([
            ServiceDirection(
                title='Хмарні архітектури',
                description='Проєктування масштабованих мікросервісів та високонавантажених відмовостійких систем.',
                icon='☁',
                sort_order=1,
            ),
            ServiceDirection(
                title='Штучний інтелект & Data Science',
                description='Інтеграція агентних систем, генеративних моделей та інтелектуальної аналітики даних.',
                icon='◉',
                sort_order=2,
            ),
            ServiceDirection(
                title='Корпоративна безпека',
                description='Комплексний аудит, криптографічний захист та відповідність стандартам ISO/IEC.',
                icon='▣',
                sort_order=3,
            ),
        ])

    if not CompanyPrinciple.objects.exists():
        CompanyPrinciple.objects.bulk_create([
            CompanyPrinciple(title='Інноваційність', description='Постійно впроваджуємо найсучасніші технологічні стандарти.', sort_order=1),
            CompanyPrinciple(title='Надійність', description='Гарантуємо найвищу стабільність інженерних продуктів і сервісів.', sort_order=2),
            CompanyPrinciple(
                title='Міжнародне партнерство',
                description='Обʼєднуємо таланти по всій Європі з представництвами у 4 ключових столицях.',
                sort_order=3,
            ),
            CompanyPrinciple(
                title='Прозорість',
                description='Відкритий діалог із клієнтами, партнерами та нашою інженерною спільнотою.',
                sort_order=4,
            ),
        ])

    if not NewsArticle.objects.exists():
        NewsArticle.objects.bulk_create([
            NewsArticle(
                title='Запуск нового технологічного кластера в Берліні у 2026 році',
                published_on=date(2026, 11, 4),
                category='Експансія',
                badge_class='badge-primary',
                summary='Компанія ZemNyux розширює європейську присутність, відкриваючи новий R&D офіс у Берліні.',
            ),
            NewsArticle(
                title='Спеціальний реліз: Yellow Submarine Enterprise Platform v4.0',
                published_on=date(2026, 10, 28),
                category='Технології',
                badge_class='badge-success',
                summary='Нова версія флагманської платформи забезпечує швидшу обробку розподілених маршрутів.',
            ),
            NewsArticle(
                title='ZemNyux отримала міжнародний сертифікат безпеки CloudTrust ISO-27001',
                published_on=date(2026, 10, 15),
                category='Безпека',
                badge_class='badge-info',
                summary='Незалежні аудитори підтвердили найвищий рівень захисту клієнтських даних.',
            ),
        ])

    if not TeamMember.objects.exists():
        TeamMember.objects.bulk_create([
            TeamMember(
                name='Олександр Смит',
                role='Генеральний директор (CEO & Founder)',
                bio='Понад 15 років керує міжнародними технологічними компаніями.',
                initials='ОС',
                sort_order=1,
            ),
            TeamMember(
                name='Марія Коваль',
                role='Технічний директор (CTO)',
                bio='Експерт з розподілених систем та штучного інтелекту.',
                initials='МК',
                sort_order=2,
            ),
            TeamMember(
                name='Дмитро Петренко',
                role='Головний системний архітектор (Lead Architect)',
                bio='Спеціалізується на масштабованих Django та Cloud-Native рішеннях.',
                initials='ДП',
                sort_order=3,
            ),
            TeamMember(
                name='Анна Шнайдер',
                role='Директорка з міжнародного розвитку (VP of Global Growth)',
                bio='Координує роботу закордонних представництв.',
                initials='АШ',
                sort_order=4,
            ),
        ])

    if not ContactOffice.objects.exists():
        offices = [
            {
                'code': 'ukraine',
                'name': 'Україна',
                'city': 'Київ / Одеса',
                'flag': 'UA',
                'short_desc': 'Головний центр розробки та досліджень.',
                'page_title': 'Контакти: Україна (Київ / Одеса)',
                'page_lead': 'Основні інженерні команди та центр технічної підтримки клієнтів',
                'related_branch_slug': '',
                'sort_order': 1,
                'locations': [
                    {
                        'title': 'Одеський інженерний хаб',
                        'address': 'вул. Дерибасівська, 25, Одеса, 65000, Україна',
                        'phone': '+380 48 700 00 00',
                        'email': 'odessa.dev@zemnyux.example',
                        'hours': '',
                    },
                    {
                        'title': 'Київський офіс звʼязків',
                        'address': 'вул. Хрещатик, 14, Київ, 01001, Україна',
                        'phone': '+380 44 200 00 00',
                        'email': 'kyiv.hq@zemnyux.example',
                        'hours': '',
                    },
                ],
            },
            {
                'code': 'france',
                'name': 'Франція',
                'city': 'Париж',
                'flag': 'FR',
                'short_desc': 'Західноєвропейський офіс звʼязків та фінансів.',
                'page_title': 'Контакти: Франція (Париж)',
                'page_lead': 'Офіс у Парижі координує роботу з європейськими партнерами та клієнтами',
                'related_branch_slug': 'paris',
                'sort_order': 2,
                'locations': [
                    {
                        'title': 'Офіс у Парижі (Паризький філіал)',
                        'address': '12 Rue de Rivoli, 75001 Paris, France',
                        'phone': '+33 1 40 50 60 70',
                        'email': 'paris.office@zemnyux.example',
                        'hours': 'Пн – Пт: 09:00 – 17:30 (CET)',
                    },
                ],
            },
            {
                'code': 'austria',
                'name': 'Австрія',
                'city': 'Відень',
                'flag': 'AT',
                'short_desc': 'Центральноєвропейський хаб клієнтської підтримки.',
                'page_title': 'Контакти: Австрія (Відень)',
                'page_lead': 'Центральноєвропейський хаб у Відні',
                'related_branch_slug': '',
                'sort_order': 3,
                'locations': [
                    {
                        'title': 'Офіс у Відні',
                        'address': 'Ringstraße 1, 1010 Wien, Austria',
                        'phone': '+43 1 234 5678',
                        'email': 'vienna.office@zemnyux.example',
                        'hours': 'Пн – Пт: 09:00 – 17:00 (CET)',
                    },
                ],
            },
            {
                'code': 'germany',
                'name': 'Німеччина',
                'city': 'Берлін',
                'flag': 'DE',
                'short_desc': 'Інноваційний R&D хаб хмарних технологій.',
                'page_title': 'Контакти: Німеччина (Берлін)',
                'page_lead': 'Німецьке представництво та R&D хаб',
                'related_branch_slug': 'berlin',
                'sort_order': 4,
                'locations': [
                    {
                        'title': 'Офіс у Берліні',
                        'address': 'Potsdamer Platz 1, 10785 Berlin, Germany',
                        'phone': '+49 30 2000 8899',
                        'email': 'berlin.office@zemnyux.example',
                        'hours': 'Пн – Пт: 09:00 – 18:00 (CET)',
                    },
                ],
            },
        ]

        for office_data in offices:
            locations = office_data.pop('locations')
            office = ContactOffice.objects.create(**office_data)
            for index, location in enumerate(locations, start=1):
                ContactLocation.objects.create(office=office, sort_order=index, **location)


def unseed_core(apps, schema_editor):
    for model_name in [
        'ContactLocation',
        'ContactOffice',
        'TeamMember',
        'NewsArticle',
        'CompanyPrinciple',
        'ServiceDirection',
        'CompanyStat',
    ]:
        apps.get_model('core', model_name).objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_core, unseed_core),
    ]
