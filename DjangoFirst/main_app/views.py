import datetime
import random
from django.shortcuts import render

DAYS_UA = {
    0: "Понеділок",
    1: "Вівторок",
    2: "Середа",
    3: "Четвер",
    4: "П'ятниця",
    5: "Субота",
    6: "Неділя",
}

QUOTES = [
    "Код пишеться один раз, а читається багато разів.",
    "Просте рішення зазвичай краще за складне.",
    "Працює — не чіпай. Розумієш як працює — покращуй.",
    "Дисципліна важливіша за натхнення.",
    "Кожна помилка — це підказка, куди дивитися далі.",
]


def home(request):
    today_index = datetime.datetime.now().weekday()
    day_name = DAYS_UA[today_index]
    quote = random.choice(QUOTES)

    context = {
        "greeting": "Hello, World!",
        "day_name": day_name,
        "quote": quote,
    }
    return render(request, "home.html", context)