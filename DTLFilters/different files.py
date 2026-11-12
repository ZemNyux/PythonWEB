views.py:
  
from decimal import Decimal
from django.shortcuts import render

def branches_list(request):
    return render(request, 'branches_list.html', {'title': 'Філії'})

def odesa(request):
    # дані для демонстрації різних фільтрів
    context = {
        'page_title': 'Демонстрація фільтрів: add, capfirst, cut, default, floatformat, join, slice, length',

        # для length, slice, join
        'products': ['кавоварка', 'кавомолка', 'турка', 'френч-прес', 'еспресо-машина', 'аеропрес'],

        # для floatformat, add
        'price': Decimal('199.9'),
        'discount': Decimal('15'),
        'negative_discount': Decimal('-15.5'),
        'quantity': 3,

        # для capfirst, cut
        'category': 'аксесуари для кави та чаю',
        'description': 'Компактна та стильна кавоварка для дому та офісу',

        # для default
        'stock': None,    # буде замінено на дефолт
        'promo_code': '', # порожній рядок > дефолт
    }

    return render(request, 'odesa.html', context)

def orleans(request):
    return render(request, 'orleans.html', {'title': 'Філія в Орлеані'})
  
==============================================================================================================

odesa.html:
  
{% extends 'base.html' %}

{% load custom_filters %} <!-- !!! -->

{% block title %}{{ page_title }}{% endblock %}

{% block content %}
<main style="max-width: 900px; margin: 0 auto; padding: 2rem 1rem;">

    <h1>Фільтри DTL: add · capfirst · cut · default · floatformat · join · slice · length</h1>
    <p style="color:#555; margin-bottom: 2.5rem;">
        Усі приклади — це один рядок у шаблоні. Не треба лізти у view за кожним дрібним перетворенням.
    </p>

    <!-- length – довжина колекції -->
    <section style="margin-bottom: 2.5rem;">
        <h3>length – кількість елементів</h3>
        <p>У нас є {{ products|length }} товарів у категорії</p>
        {% if products|length > 5 %}
        <p style="color: green;">Асортимент великий — є з чого вибрати!</p>
        {% endif %}
    </section>

    <!-- join – об’єднання списку в рядок -->
    <section style="margin-bottom: 2.5rem;">
        <h3>join – склеювання списку</h3>
        <p>Наші товари: {{ products|join:", " }}</p>
        <p>З роздільником: {{ products|join:" | " }}</p>
    </section>

    <!-- slice – зріз списку -->
    <section style="margin-bottom: 2.5rem;">
        <h3>slice – взяти частину списку</h3>
        <p>Перші 3 товари: {{ products|slice:":3"|join:", " }}</p>
        <p>Товари з 2 по 5: {{ products|slice:"1:5"|join:", " }}</p>
        <p>Останні 2: {{ products|slice:"-2:"|join:", " }}</p>
    </section>

    <!-- add – додавання числа -->
    <section style="margin-bottom: 2.5rem;">
        <h3>add – проста математика</h3>
        <p>Ціна: {{ price }} грн</p>
        <p>Знижка 15 грн спеціально для вас: нова ціна {{ price|add:negative_discount|floatformat:2 }} грн</p>
        <!-- розрахунки краще робити у view, результат бачите самі, 184.00 замість 184.39 -->
        <!-- більшість вбудованих фільтрів DTL (включаючи floatformat, add) працюють з float, а не з Decimal -->
        <p>Знижка 15% спеціально для вас: нова ціна {{ price|percent_off:discount }} грн</p>
    </section>

    <!-- floatformat – форматування чисел -->
    <section style="margin-bottom: 2.5rem;">
        <h3>floatformat – гарне число</h3>
        <p>Ціна без копійок: {{ price|floatformat:0 }} грн</p>
        <p>З двома знаками: {{ price|floatformat:2 }} грн</p>
    </section>

    <!-- capfirst – велика перша літера -->
    <section style="margin-bottom: 2.5rem;">
        <h3>capfirst – перша літера велика</h3>
        <p>Категорія: {{ category|capfirst }}</p>
        <p>Опис: {{ description|capfirst }}</p>
    </section>

    <!-- cut – видалення символів -->
    <section style="margin-bottom: 2.5rem;">
        <h3>cut – прибрати символи</h3>
        <p>Оригінал: {{ description }}</p>
        <p>Без пробілів: {{ description|cut:" " }}</p>
        <p>Без букв "а": {{ description|cut:"а" }}</p>
    </section>

    <!-- default – значення за замовчуванням -->
    <section>
        <h3>default – якщо значення немає або порожнє</h3>
        <p>Залишок на складі: {{ stock|default:"немає в наявності" }}</p>
        <p>Промокод: {{ promo_code|default:"немає промокоду" }}</p>
        <p>Кількість відгуків: {{ reviews_count|default:"0" }}</p>
    </section>

</main>
{% endblock %}

==============================================================================================================

company_site / branches / templatetags / custom_filters.py (папку та файл треба створити!):

from decimal import Decimal, InvalidOperation
from django import template

# кастомний фільтр для віднімання відсотка від ціни

register = template.Library() # реєструємо бібліотеку, щоб Django знав, що тут є фільтри

@register.filter
def percent_off(price, percent):
    """
    Віднімає відсоток від ціни.
    Використання: {{ price|percent_off:15.5 }}
    """
    try:
        # перетворюємо percent у Decimal для точності
        percent = Decimal(str(percent)) # str щоб уникнути похибки float
        discount = price * (percent / Decimal('100'))
        result = price - discount
        # повертаємо Decimal з 2 знаками після коми
        return result.quantize(Decimal('0.01'))
    except (ValueError, TypeError, InvalidOperation):
        return price # якщо щось не так — повертаємо оригінал