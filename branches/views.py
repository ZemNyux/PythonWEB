from django.shortcuts import render


def branches_list(request):
  return render(request, 'branches_list.html', context={'title': 'Філії'})


def london(request):
  return render(request, 'london.html', context={'title': 'Філія в Лондоні'})


def paris(request):
  return render(request, 'paris.html', context={'title': 'Філія в Парижі'})


# Обязательно с return render(...)!
def history_main(request):
  return render(request, 'history.html', context={'title': 'Історія міста'})


def history_dates(request):
  return render(request, 'dates.html', context={'title': 'Перелік дат'})


def history_facts(request):
  return render(request, 'facts.html', context={'title': 'Значущі факти'})