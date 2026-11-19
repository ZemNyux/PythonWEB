from django.shortcuts import get_object_or_404, render

from .models import Branch, CompanyFact, HistoryEvent


def branches_list(request):
    branches = Branch.objects.all()
    return render(
        request,
        'branches_list.html',
        context={'title': 'Міжнародні філії компанії', 'branches': branches},
    )


def branch_detail(request, slug):
    branch = get_object_or_404(Branch, slug__iexact=slug)
    return render(
        request,
        'branch_detail.html',
        context={
            'title': branch.page_title,
            'branch': branch,
        },
    )


def history_main(request):
    return render(
        request,
        'history.html',
        context={
            'title': 'Історія компанії та філій',
            'intro': (
                'Від заснування інженерної лабораторії до формування міжнародної мережі '
                'технологічних центрів у ключових столицях Європи.'
            ),
        },
    )


def history_dates(request):
    timeline = HistoryEvent.objects.all()
    return render(
        request,
        'dates.html',
        context={'title': 'Хронологія розвитку та дати', 'timeline': timeline},
    )


def history_facts(request):
    facts = CompanyFact.objects.all()
    return render(
        request,
        'facts.html',
        context={'title': 'Значущі факти про нас', 'facts': facts},
    )
