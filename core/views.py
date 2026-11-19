from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .entities import LeaderProfile, MetricCard, ServiceOffer
from .forms import ContactInquiryForm
from .models import (
    CompanyPrinciple,
    CompanyStat,
    ContactOffice,
    NewsArticle,
    ServiceDirection,
    TeamMember,
)


def home(request):
    db_stats = list(CompanyStat.objects.all())
    db_services = list(ServiceDirection.objects.all())

    metric_objects = [
        MetricCard(
            value=stat.value,
            label=stat.label,
            is_highlight=(index == 0),
        )
        for index, stat in enumerate(db_stats)
    ] or [
        MetricCard('12+', 'Років на ринку', is_highlight=True),
        MetricCard('4', 'Міжнародні філії'),
        MetricCard('180+', 'Реалізованих проєктів'),
    ]

    service_objects = [
        ServiceOffer(
            title=service.title,
            description=service.description,
            icon=service.icon or '◆',
            is_featured=(index == 0),
        )
        for index, service in enumerate(db_services)
    ] or [
        ServiceOffer('Хмарні архітектури', 'Масштабовані мікросервіси.', '☁', True),
        ServiceOffer('Штучний інтелект', 'Агентні системи та аналітика.', '◉'),
    ]

    portal_data = {
        'hero': {
            'company_name': 'ZemNyux Inc.',
            'tagline': 'Передові інженерні та програмні рішення для глобального бізнесу',
            'year': 2026,
        },
        'dashboard': {
            'metrics': metric_objects,
            'services': service_objects,
            'show_featured_only': False,
        },
        'shortcuts': {
            'items': [
                {
                    'title': 'Міжнародні філії',
                    'text': 'Хаби в Лондоні, Парижі та Берліні.',
                    'url_name': 'branches_list',
                    'badge': 'Розділ',
                    'badge_class': 'badge-primary',
                },
                {
                    'title': 'Останні анонси',
                    'text': 'Релізи платформи та сертифікації.',
                    'url_name': 'news',
                    'badge': 'Новини',
                    'badge_class': 'badge-success',
                },
                {
                    'title': 'Контакти офісів',
                    'text': 'Представництва в Україні та Європі.',
                    'url_name': 'contacts',
                    'badge': "Зв'язок",
                    'badge_class': 'badge-info',
                },
            ],
        },
    }

    return render(
        request,
        'home.html',
        {
            'title': 'Головна сторінка',
            'portal_data': portal_data,
            'stats': db_stats,
            'services': db_services,
        },
    )


def news(request):
    articles = NewsArticle.objects.filter(is_published=True)
    news_payload = {
        'section': {
            'title': 'Новини компанії',
            'articles': list(articles),
        },
        'meta': {
            'total': articles.count(),
            'has_articles': articles.exists(),
        },
    }
    return render(
        request,
        'news.html',
        {
            'title': 'Новини компанії',
            'articles': articles,
            'news_payload': news_payload,
        },
    )


def management(request):
    members = list(TeamMember.objects.all())
    leader_objects = [
        LeaderProfile(
            name=member.name,
            role=member.role,
            bio=member.bio,
            initials=member.initials,
            phone=['+380441111111', '+380442222222', '+380443333333', '+4402079460991'][index % 4],
            is_executive=(index < 2),
        )
        for index, member in enumerate(members)
    ] or [
        LeaderProfile(
            name='Олександр Смит',
            role='CEO',
            bio='Стратегічний розвиток.',
            initials='ОС',
            phone='+380441111111',
            is_executive=True,
        ),
    ]

    board_data = {
        'company': {
            'name': 'ZemNyux Inc.',
            'board_title': 'Рада директорів',
        },
        'leaders': {
            'profiles': leader_objects,
            'hotline': '+3808005002026',
        },
    }

    return render(
        request,
        'management.html',
        {
            'title': 'Керівництво компанії',
            'team': members,
            'board_data': board_data,
        },
    )


def about(request):
    principles = list(CompanyPrinciple.objects.all())
    about_data = {
        'mission': {
            'title': 'Про компанію',
            'principles': principles,
            'is_public': True,
        }
    }
    return render(
        request,
        'about.html',
        {
            'title': 'Про компанію',
            'principles': principles,
            'about_data': about_data,
        },
    )


def contacts(request, country=None):
    if country is None:
        form = ContactInquiryForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, 'Дякуємо! Ваш запит збережено.')
                return redirect('contacts')
            messages.error(request, 'Перевірте поля форми та спробуйте ще раз.')

        countries = ContactOffice.objects.all()
        return render(
            request,
            'contacts.html',
            {
                'title': 'Контакти представництв',
                'countries': countries,
                'form': form,
            },
        )

    office = get_object_or_404(ContactOffice, code__iexact=country)
    return render(
        request,
        'contact_country.html',
        {
            'title': office.page_title,
            'office': office,
            'locations': office.locations.all(),
            'country_code': office.code,
        },
    )


def custom_404_view(request, exception=None):
    return render(
        request,
        '404.html',
        {
            'title': '404 — Сторінку не знайдено',
            'requested_path': request.path,
        },
        status=404,
    )
