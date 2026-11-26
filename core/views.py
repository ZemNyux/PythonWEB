from django.contrib import messages
from django.contrib.auth.views import redirect_to_login
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils.http import url_has_allowed_host_and_scheme

from .accounts_memory import account_for_username, authenticate_account, create_account
from .entities import LeaderProfile, MetricCard, ServiceOffer
from .forms import AccountLoginForm, ContactInquiryForm, ProductComplaintForm, RegistrationForm
from .models import (
    CompanyPrinciple,
    CompanyStat,
    ContactOffice,
    NewsArticle,
    ServiceDirection,
    TeamMember,
)


def _current_site_account(request):
    username = request.session.get('site_username')
    account = account_for_username(username) if username else None
    if username and not account:
        request.session.pop('site_username', None)
    return account


def home(request):
    account = _current_site_account(request)
    if not account:
        return redirect_to_login(request.get_full_path(), login_url=reverse('account_login'))

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
            'account': account,
            'portal_data': portal_data,
            'stats': db_stats,
            'services': db_services,
        },
    )


def account_register(request):
    if _current_site_account(request):
        return redirect('home')

    form = RegistrationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        try:
            account = create_account(
                form.cleaned_data['username'],
                form.cleaned_data['email'],
                form.cleaned_data['password'],
            )
        except ValueError as error:
            form.add_error(None, str(error))
        else:
            request.session.cycle_key()
            request.session['site_username'] = account['username']
            return redirect('home')

    return render(request, 'registration/register.html', {'title': 'Реєстрація', 'form': form})


def account_login(request):
    if _current_site_account(request):
        return redirect('home')

    form = AccountLoginForm(request.POST or None)
    next_url = request.POST.get('next', request.GET.get('next', ''))
    if request.method == 'POST' and form.is_valid():
        account = authenticate_account(form.cleaned_data['username'], form.cleaned_data['password'])
        if account:
            request.session.cycle_key()
            request.session['site_username'] = account['username']
            if next_url and url_has_allowed_host_and_scheme(
                next_url,
                allowed_hosts={request.get_host()},
                require_https=request.is_secure(),
            ):
                return redirect(next_url)
            return redirect('home')
        form.add_error(None, 'Неправильний логін або пароль.')

    return render(
        request,
        'registration/login.html',
        {'title': 'Вхід', 'form': form, 'next': next_url},
    )


@require_POST
def account_logout(request):
    request.session.flush()
    return redirect('account_login')


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


def product_complaint(request):
    form = ProductComplaintForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        return render(
            request,
            'product_complaint_result.html',
            {
                'title': 'Скаргу оформлено',
                'complaint': form.cleaned_data,
            },
        )
    return render(
        request,
        'product_complaint.html',
        {
            'title': 'Скарга на товар',
            'form': form,
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
