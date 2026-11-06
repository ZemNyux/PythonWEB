from django.http import Http404
from django.shortcuts import render

CONTACT_PAGES = {
    'france': ('france.html', 'Контакти: Франція (Париж)'),
    'ukraine': ('ukraine.html', 'Контакти: Україна (Київ / Одеса)'),
    'austria': ('austria.html', 'Контакти: Австрія (Відень)'),
    'germany': ('germany.html', 'Контакти: Німеччина (Берлін)'),
}


def home(request):
    context = {
        'title': 'Головна сторінка',
        'company_name': 'ZemNyux Inc.',
        'tagline': 'Передові інженерні та програмні рішення для глобального бізнесу',
        'stats': [
            {'num': '12+', 'label': 'Років на ринку'},
            {'num': '4', 'label': 'Міжнародні філії'},
            {'num': '180+', 'label': 'Реалізованих проєктів'},
            {'num': '99.9%', 'label': 'Безвідмовність систем'},
        ],
        'services': [
            {
                'title': 'Хмарні архітектури',
                'desc': 'Проєктування масштабованих мікросервісів та високонавантажених відмовостійких систем.',
                'icon': '☁️',
            },
            {
                'title': 'Штучний інтелект & Data Science',
                'desc': 'Інтеграція агентних систем, генеративних моделей та інтелектуальної аналітики даних.',
                'icon': '🤖',
            },
            {
                'title': 'Корпоративна безпека',
                'desc': 'Комплексний аудит, криптографічний захист та відповідність стандартам ISO/IEC.',
                'icon': '🛡️',
            },
        ],
    }
    return render(request, 'home.html', context)


def news(request):
    articles = [
        {
            'title': 'Запуск нового технологічного кластера в Берліні у 2026 році',
            'date': '04 Листопада 2026',
            'category': 'Експансія',
            'badge_class': 'badge-primary',
            'summary': 'Компанія ZemNyux розширює європейську присутність, відкриваючи новий R&D офіс у Берліні для розробки ШІ-рішень нового покоління.',
        },
        {
            'title': 'Спеціальний реліз: Yellow Submarine Enterprise Platform v4.0',
            'date': '28 Жовтня 2026',
            'category': 'Технології',
            'badge_class': 'badge-success',
            'summary': 'Нова версія флагманської платформи забезпечує на 40% швидшу обробку розподілених маршрутів та захищене шифрування даних.',
        },
        {
            'title': 'ZemNyux отримала міжнародний сертифікат безпеки CloudTrust ISO-27001',
            'date': '15 Жовтня 2026',
            'category': 'Безпека',
            'badge_class': 'badge-info',
            'summary': 'Незалежні аудитори підтвердили найвищий рівень захисту клієнтських даних у всіх європейських та українських дата-центрах.',
        },
    ]
    return render(request, 'news.html', {'title': 'Новини компанії', 'articles': articles})


def management(request):
    team = [
        {
            'name': 'Олександр Смит',
            'role': 'Генеральний директор (CEO & Founder)',
            'bio': 'Понад 15 років керує міжнародними технологічними компаніями. Спрямовує стратегічний розвиток та глобальні партнерства.',
            'initials': 'ОС',
        },
        {
            'name': 'Марія Коваль',
            'role': 'Технічний директор (CTO)',
            'bio': 'Експерт з розподілених систем та штучного інтелекту. Керує архітектурним напрямом і дослідженнями R&D.',
            'initials': 'МК',
        },
        {
            'name': 'Дмитро Петренко',
            'role': 'Головний системний архітектор (Lead Architect)',
            'bio': 'Спеціалізується на масштабованих Django та Cloud-Native рішеннях із надвисокими вимогами до швидкодії.',
            'initials': 'ДП',
        },
        {
            'name': 'Анна Шнайдер',
            'role': 'Директорка з міжнародного розвитку (VP of Global Growth)',
            'bio': 'Координує роботу закордонних представництв у Великій Британії, Франції, Австрії та Німеччині.',
            'initials': 'АШ',
        },
    ]
    return render(request, 'management.html', {'title': 'Керівництво компанії', 'team': team})


def about(request):
    context = {
        'title': 'Про компанію',
        'principles': [
            {'title': 'Інноваційність', 'desc': 'Постійно впроваджуємо найсучасніші технологічні стандарти.'},
            {'title': 'Надійність', 'desc': 'Гарантуємо найвищу стабільність інженерних продуктів і сервісів.'},
            {'title': 'Міжнародне партнерство', 'desc': 'Об’єднуємо таланти по всій Європі з представництвами у 4 ключових столицях.'},
            {'title': 'Прозорість', 'desc': 'Відкритий діалог із клієнтами, партнерами та нашою інженерною спільнотою.'},
        ],
    }
    return render(request, 'about.html', context)


def contacts(request, country=None):
    if country is None:
        countries = [
            {'code': 'ukraine', 'name': 'Україна', 'city': 'Київ / Одеса', 'flag': '🇺🇦', 'desc': 'Головний центр розробки та досліджень.'},
            {'code': 'france', 'name': 'Франція', 'city': 'Париж', 'flag': '🇫🇷', 'desc': 'Західноєвропейський офіс зв’язків та фінансів.'},
            {'code': 'austria', 'name': 'Австрія', 'city': 'Відень', 'flag': '🇦🇹', 'desc': 'Центральноєвропейський хаб клієнтської підтримки.'},
            {'code': 'germany', 'name': 'Німеччина', 'city': 'Берлін', 'flag': '🇩🇪', 'desc': 'Інноваційний R&D хаб хмарних технологій.'},
        ]
        return render(request, 'contacts.html', {'title': 'Контакти представництв', 'countries': countries})

    page = CONTACT_PAGES.get(country.lower())
    if page is None:
        raise Http404('Представництво у вказаній країні не знайдено')

    template, title = page
    return render(request, template, {'title': title, 'country_code': country.lower()})


def custom_404_view(request, exception=None):
    """Кастомна сторінка для обробки помилок 404 (неіснуючий розділ)"""
    return render(
        request,
        '404.html',
        {
            'title': '404 — Сторінку не знайдено',
            'requested_path': request.path,
        },
        status=404,
    )
