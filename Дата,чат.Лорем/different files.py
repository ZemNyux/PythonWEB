branches / views.py:

from django.shortcuts import render
from datetime import datetime, timedelta, date, time

def branches_list(request):
    return render(request, 'branches_list.html', {'title': 'Філії'})

def odesa(request):
    # різні об'єкти дати/часу
    now = datetime.now()                         # поточний момент
    past_event = datetime(2025, 12, 31, 23, 59)  # приклад події в минулому
    future_event = datetime(2027, 7, 15, 14, 30) # приклад події в майбутньому
    only_date = date(2026, 3, 3)                 # тільки дата
    only_time = time(9, 41, 22)                  # тільки час

    # для timesince / timeuntil — різниця в часі
    company_birth = datetime(2006, 10, 15)

    context = {
        'page_title': 'Філія в Одесі – приклади дати, часу та lorem ipsum',
        'current_year': now.year,

        'now': now,
        'past_event': past_event,
        'future_event': future_event,
        'only_date': only_date,
        'only_time': only_time,
        'company_birth': company_birth,
    }

    return render(request, 'odesa.html', context)

def orleans(request):
    return render(request, 'orleans.html', {'title': 'Філія в Орлеані'})
  
================================================================================================================================

branches / templates / odesa.html:
    
    
{% extends 'base.html' %}

{% block title %}{{ page_title }}{% endblock %}

{% block content %}
<main class="main-branch" style="max-width: 900px; margin: 0 auto; padding: 2rem 1rem;">

    <h1>Демонстрація роботи з датою, часом та lorem ipsum</h1>
    <p style="color:#555; margin-bottom: 2.5rem;">
        Усі приклади нижче — це один рядок у шаблоні. Без них доводилося б писати методи в моделях або обробляти дані у view.
    </p>

    <!-- поточний момент -->
    <section style="margin-bottom: 2.5rem;">
        <h3>Поточний момент (now)</h3>
        <p>Сирий вигляд: {{ now }}</p>
        <ul>
            <li>Коротка дата: {{ now|date:"d.m.Y" }}</li>
            <li>Повна дата українською: {{ now|date:"d F Y" }}</li>
            <li>З днем тижня: {{ now|date:"l, d F Y" }}</li>
            <li>Дата + час: {{ now|date:"d F Y H:i" }}</li>
            <li>Тільки час: {{ now|time:"H:i:s" }}</li>
            <li>Короткий формат (SHORT_DATETIME_FORMAT): {{ now|date:"SHORT_DATETIME_FORMAT" }}</li>
        </ul>
    </section>

    <!-- окремо дата та час -->
    <section style="margin-bottom: 2.5rem;">
        <h3>Тільки дата та тільки час</h3>
        <p>Тільки дата: {{ only_date }} > {{ only_date|date:"d F Y" }}</p>
        <p>Тільки час: {{ only_time }} > {{ only_time|time:"H:i" }}</p>
    </section>

    <!-- різниця в часі (timesince / timeuntil) -->
    <section style="margin-bottom: 2.5rem;">
        <h3>Різниця в часі (timesince / timeuntil)</h3>
        <p>Компанія працює вже: {{ company_birth|timesince }}</p>
        <p>Новий рік 2026 був: {{ past_event|timesince }} тому</p>
        <p>До події в 2027: {{ future_event|timeuntil }}</p>
    </section>

    <!-- формати з параметрами та кастомні -->
    <section style="margin-bottom: 2.5rem;">
        <h3>Корисні формати та трюки</h3>
        <ul>
            <li>Тільки рік: {{ now|date:"Y" }}</li>
            <li>Місяць словом + рік: {{ now|date:"F Y" }}</li>
            <li>Час без секунд: {{ now|time:"H:i" }}</li>
            <li>Дата у форматі ISO: {{ now|date:"Y-m-d" }}</li>
            <li>Час у 12-годинному форматі: {{ now|time:"g:i A" }}</li>
        </ul>
    </section>

    <!-- Lorem ipsum – ідеально для прототипів -->
    <section>
        <h3>lorem ipsum – заповнювач тексту</h3>
        <p style="font-style: italic; color: #666;">Приклади генерації тексту без копіювання з інтернету:</p>

        <div style="margin: 1.5rem 0; padding: 1rem; background: #f0f4f8; border-radius: 6px;">
            <strong>1 абзац:</strong><br>
            {% lorem 1 p %}
        </div>

        <div style="margin: 1.5rem 0; padding: 1rem; background: #f0f4f8; border-radius: 6px;">
            <strong>2 абзаци:</strong><br>
            {% lorem 2 p %}
        </div>

        <div style="margin: 1.5rem 0; padding: 1rem; background: #f0f4f8; border-radius: 6px;">
            <strong>40 слів:</strong><br>
            {% lorem 40 w %}
        </div>

        <div style="margin: 1.5rem 0; padding: 1rem; background: #f0f4f8; border-radius: 6px;">
            <strong>5 речень:</strong><br>
            {% lorem 5 b %}
        </div>

        <p style="margin-top: 2rem; font-size: 0.95rem; color: #555;">
            Ці інструменти економлять величезну кількість часу при створенні прототипів, демо-сторінок та заповненні тестових даних.
        </p>
    </section>

</main>
{% endblock %}