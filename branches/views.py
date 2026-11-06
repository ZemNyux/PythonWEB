from django.shortcuts import render


def branches_list(request):
    branches = [
        {
            'name': 'Лондон (Велика Британія)',
            'city': 'Лондон',
            'url_name': 'london',
            'focus': 'Фінтех, хмарні системи та міжнародні інвестиційні проєкти.',
            'address': 'One Canada Square, Canary Wharf, London, E14 5AA',
            'phone': '+44 20 7946 0991',
            'tag': 'Фінтех-хаб',
        },
        {
            'name': 'Париж (Франція)',
            'city': 'Париж',
            'url_name': 'paris',
            'focus': 'Дизайн систем, UI/UX лаб та європейські публічні партнерства.',
            'address': '12 Rue de Rivoli, 75001 Paris',
            'phone': '+33 1 40 50 60 70',
            'tag': 'Інновації',
        },
        {
            'name': 'Берлін (Німеччина)',
            'city': 'Берлін',
            'url_name': 'berlin',
            'focus': 'R&D центр штучного інтелекту та кібербезпеки.',
            'address': 'Potsdamer Platz 1, 10785 Berlin',
            'phone': '+49 30 2000 8899',
            'tag': 'R&D Центр',
        },
    ]
    return render(
        request,
        'branches_list.html',
        context={'title': 'Міжнародні філії компанії', 'branches': branches},
    )


def london(request):
    return render(
        request,
        'london.html',
        context={
            'title': 'Філія в Лондоні',
            'city': 'Лондон',
            'established': '2015',
            'specialization': 'Фінтех, блокчейн та хмарна архітектура',
            'address': 'One Canada Square, Canary Wharf, London, E14 5AA',
            'phone': '+44 20 7946 0991',
            'email': 'london.office@zemnyux.example',
        },
    )


def paris(request):
    return render(
        request,
        'paris.html',
        context={
            'title': 'Філія в Парижі',
            'city': 'Париж',
            'established': '2018',
            'specialization': 'UX-лабораторії, фронтенд-інженерія та цифрова трансформація',
            'address': '12 Rue de Rivoli, 75001 Paris',
            'phone': '+33 1 40 50 60 70',
            'email': 'paris.office@zemnyux.example',
        },
    )


def berlin(request):
    return render(
        request,
        'berlin.html',
        context={
            'title': 'Філія в Берліні',
            'city': 'Берлін',
            'established': '2024',
            'specialization': 'Дослідження машинного навчання, агентних ШІ та захисту даних',
            'address': 'Potsdamer Platz 1, 10785 Berlin',
            'phone': '+49 30 2000 8899',
            'email': 'berlin.office@zemnyux.example',
        },
    )


def history_main(request):
    return render(
        request,
        'history.html',
        context={
            'title': 'Історія компанії та філій',
            'intro': 'Від заснування інженерної лабораторії до формування міжнародної мережі технологічних центрів у ключових столицях Європи.',
        },
    )


def history_dates(request):
    timeline = [
        {
            'year': '1878',
            'event': 'Закладено перші інженерні та торгові традиції, які стали фундаментом нашої корпоративної філософії.',
        },
        {
            'year': '1945',
            'event': 'Повоєнне відновлення підприємства та фокус на європейську співпрацю й відновлення інфраструктури.',
        },
        {
            'year': '2012',
            'event': 'Заснування бренду ZemNyux у сфері інформаційних технологій та розробки програмного забезпечення.',
        },
        {
            'year': '2015',
            'event': 'Відкриття лондонського представництва, вихід на глобальний ринок фінансових технологій.',
        },
        {
            'year': '2018',
            'event': 'Запуск паризької філії та масштабування команди інженерів до 100+ осіб.',
        },
        {
            'year': '2026',
            'event': 'Відкриття хабу в Берліні, запуск нової лінійки інноваційних продуктів Yellow Submarine.',
        },
    ]
    return render(request, 'dates.html', context={'title': 'Хронологія розвитку та дати', 'timeline': timeline})


def history_facts(request):
    facts = [
        {
            'badge': 'Факт 1',
            'title': 'Розподілена мережа без кордонів',
            'text': 'Усі філії компанії використовують єдину децентралізовану інфраструктуру з нульовим часом простою.',
        },
        {
            'badge': 'Факт 2',
            'title': 'Зелені дата-центри',
            'text': 'Офіси в Лондоні, Парижі та Берліні на 100% живляться з відновлюваних джерел енергії (Green Computing).',
        },
        {
            'badge': 'Факт 3',
            'title': 'Культура менторства',
            'text': 'Більше 40% наших провідних архітекторів виросли всередині компанії через внутрішню програму стажування.',
        },
        {
            'badge': 'Факт 4',
            'title': 'Відкритий код (Open Source)',
            'text': 'ZemNyux активно підтримує екосистему Python та Django, роблячи внесок у бібліотеки та відкриті інструменти.',
        },
    ]
    return render(request, 'facts.html', context={'title': 'Значущі факти про нас', 'facts': facts})
