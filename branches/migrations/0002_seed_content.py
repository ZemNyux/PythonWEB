from django.db import migrations


def seed_branches(apps, schema_editor):
    Branch = apps.get_model('branches', 'Branch')
    HistoryEvent = apps.get_model('branches', 'HistoryEvent')
    CompanyFact = apps.get_model('branches', 'CompanyFact')

    if not Branch.objects.exists():
        Branch.objects.bulk_create([
            Branch(
                slug='london',
                name='Лондон (Велика Британія)',
                city='Лондон',
                tag='Фінтех-хаб',
                focus='Фінтех, хмарні системи та міжнародні інвестиційні проєкти.',
                address='One Canada Square, Canary Wharf, London, E14 5AA',
                phone='+44 20 7946 0991',
                email='london.office@zemnyux.example',
                established=2015,
                specialization='Фінтех, блокчейн та хмарна архітектура',
                page_title='Філія в Лондоні',
                page_lead='Провідний європейський фінтех-хаб та інноваційний центр розподілених систем',
                detail_intro=(
                    'Лондонський офіс функціонує з 2015 року та розташований у діловому серці столиці — '
                    'Кенері-Ворф. Команда спеціалізується на розробці високошвидкісних фінансових шлюзів.'
                ),
                sort_order=1,
            ),
            Branch(
                slug='paris',
                name='Париж (Франція)',
                city='Париж',
                tag='Інновації',
                focus='Дизайн систем, UI/UX лаб та європейські публічні партнерства.',
                address='12 Rue de Rivoli, 75001 Paris',
                phone='+33 1 40 50 60 70',
                email='paris.office@zemnyux.example',
                established=2018,
                specialization='UX-лабораторії, фронтенд-інженерія та цифрова трансформація',
                page_title='Філія в Парижі',
                page_lead='Центр інновацій та дизайну в Парижі',
                detail_intro=(
                    'Паризька філія поєднує продуктові дослідження, UX-лабораторії та партнерства '
                    'з європейськими інституціями.'
                ),
                sort_order=2,
            ),
            Branch(
                slug='berlin',
                name='Берлін (Німеччина)',
                city='Берлін',
                tag='R&D Центр',
                focus='R&D центр штучного інтелекту та кібербезпеки.',
                address='Potsdamer Platz 1, 10785 Berlin',
                phone='+49 30 2000 8899',
                email='berlin.office@zemnyux.example',
                established=2024,
                specialization='Дослідження машинного навчання, агентних ШІ та захисту даних',
                page_title='Філія в Берліні',
                page_lead='R&D кластер штучного інтелекту в Берліні',
                detail_intro=(
                    'Берлінський хаб зосереджений на дослідженнях ШІ, захисті даних і хмарній інфраструктурі '
                    'нового покоління.'
                ),
                sort_order=3,
            ),
        ])

    if not HistoryEvent.objects.exists():
        HistoryEvent.objects.bulk_create([
            HistoryEvent(year='1878', event='Закладено перші інженерні та торгові традиції.', sort_order=1),
            HistoryEvent(year='1945', event='Повоєнне відновлення підприємства та фокус на європейську співпрацю.', sort_order=2),
            HistoryEvent(year='2012', event='Заснування бренду ZemNyux у сфері інформаційних технологій.', sort_order=3),
            HistoryEvent(year='2015', event='Відкриття лондонського представництва.', sort_order=4),
            HistoryEvent(year='2018', event='Запуск паризької філії та масштабування команди інженерів.', sort_order=5),
            HistoryEvent(year='2026', event='Відкриття хабу в Берліні та запуск Yellow Submarine.', sort_order=6),
        ])

    if not CompanyFact.objects.exists():
        CompanyFact.objects.bulk_create([
            CompanyFact(
                badge='Факт 1',
                title='Розподілена мережа без кордонів',
                text='Усі філії компанії використовують єдину децентралізовану інфраструктуру.',
                sort_order=1,
            ),
            CompanyFact(
                badge='Факт 2',
                title='Зелені дата-центри',
                text='Офіси в Лондоні, Парижі та Берліні на 100% живляться з відновлюваних джерел енергії.',
                sort_order=2,
            ),
            CompanyFact(
                badge='Факт 3',
                title='Культура менторства',
                text='Більше 40% провідних архітекторів виросли всередині компанії.',
                sort_order=3,
            ),
            CompanyFact(
                badge='Факт 4',
                title='Відкритий код (Open Source)',
                text='ZemNyux підтримує екосистему Python та Django.',
                sort_order=4,
            ),
        ])


def unseed_branches(apps, schema_editor):
    for model_name in ['Branch', 'HistoryEvent', 'CompanyFact']:
        apps.get_model('branches', model_name).objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ('branches', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_branches, unseed_branches),
    ]
