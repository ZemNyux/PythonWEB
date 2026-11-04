import datetime
from asgiref.sync import async_to_sync, sync_to_async # імпорт для роботи з асинхронними методами в класових виглядах
from django.views import View
from django.views.generic import TemplateView, ListView # імпорт базових класів для створення класових виглядів (CBV) та шаблонних виглядів (TemplateView, ListView)
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import asyncio
import httpx
import time

#######################################################################################################
# простий синхронний Class Based Viev
class HelloSyncView(View):
    count = 0  # static attribute

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.count = 0
        print("HelloSyncView object has been created")

    def get(self, request):
        print("GET CONTROLLER CLASS !!! P45")
        HelloSyncView.count += 1

        return HttpResponse("<h1>" + str(HelloSyncView.count) + "</h1>")


#######################################################################################################
# асинхронний CBV (View з async-методами)
class HelloAsyncView(View):
    """Асинхронний класовий вигляд"""

    async def get(self, request):
        await asyncio.sleep(0.2) # імітація асинхронної роботи
        return HttpResponse("<h1>Привіт з асинхронного CBV!</h1>")

    async def post(self, request):
        name = request.POST.get("name", "Гість")
        return HttpResponse(f"<h2>Привіт, {name}!</h2>")

#######################################################################################################
# можливо, ви тут згадали, що в контролерах асп.нет кор можна було зробити декілька методів на гет або пост,
# але в Django це не підтримується, тому що Django використовує один метод для обробки кожного HTTP-методу
# (наприклад, get(), post(), put() і т.д.). якщо потрібно обробити різні дії в залежності від параметрів запиту,
# можна зробити це всередині одного методу, наприклад:

class MultiGetView(View):
    """
    Клас з кількома "GET"-методами з різними назвами.
    dispatch вирішує, який саме метод викликати.
    """

    def dispatch(self, request, *args, **kwargs):
        # отримуємо параметр action з GET (наприклад ?action=welcome)
        action = request.GET.get('action', 'default')

        # вибираємо потрібний обробник
        if action == 'welcome':
            return self.handle_welcome(request, *args, **kwargs)
        
        elif action == 'time':
            return self.handle_time(request, *args, **kwargs)
        
        elif action == 'info':
            return self.handle_info(request, *args, **kwargs)
        
        else:
            return self.handle_default(request, *args, **kwargs)

    # окремі методи для різних GET-сценаріїв

    def handle_default(self, request):
        return HttpResponse("<h1>Це базовий GET-метод</h1><p>Додай ?action=welcome або ?action=time</p>")

    def handle_welcome(self, request):
        return HttpResponse("<h1>Ласкаво просимо!</h1><p>Ви на сторінці привітання</p>")

    def handle_time(self, request):
        now = datetime.now().strftime("%H:%M:%S")
        return HttpResponse(f"<h1>Поточний час: {now}</h1><p>Оновлено в реальному часі</p>")

    def handle_info(self, request):
        return HttpResponse("""
            <h1>Інформація про сторінку</h1>
            <p>Це приклад з кількома GET-обробниками в одному класі.</p>
            <ul>
                <li>/?action=welcome — привітання</li>
                <li>/?action=time — час</li>
                <li>/?action=info — ця сторінка</li>
            </ul>
        """)

# у Django Class-Based Views (View та його нащадки) є зарезервовані назви методів,
# які Django викликає автоматично в певному порядку. якщо перевизначити ці методи — 
# можна буде контролювати поведінку подання. список методів:
# - dispatch(), це перший метод, який викликається Django", часто перевизначається, вирішує який HTTP-метод викликати (get/post тощо)
# - http_method_names, це список дозволених HTTP-методів (за замовчуванням ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']), список можна обмежити, наприклад, http_method_names = ['get', 'post'] для дозволу тільки GET та POST
# - get()
# - post()
# - put(), patch(), delete()
# - head(), HEAD-запит, якщо потрібні тільки заголовки (без тіла), скажімо для перевірки існування ресурсу


#######################################################################################################
# асинхронний TemplateView (з реальним async-запитом)
# TemplateView - це класове подання, яке автоматично рендерить шаблон і передає в нього контекст

import httpx
from django.views.generic import TemplateView


class WeatherAsyncTemplateView(TemplateView):
  template_name = 'weather/weather.html'

  async def get(self, request, *args, **kwargs):
    async with httpx.AsyncClient() as client:
      response = await client.get(
          'https://api.open-meteo.com/v1/forecast',
          params={
              'latitude': 42.6975,
              'longitude': 23.3242,
              'current_weather': 'true',
          },
      )

    data = response.json()['current_weather']

    context = {
        'city': 'Софія',
        'temperature': data['temperature'],
        'wind': data['windspeed'],
    }

    return self.render_to_response(context)

# специфічні методи для Generic Views (TemplateView, ListView тощо):
# - get_context_data(), повертає словник контексту для шаблону
# - get_template_names(), повертає список шаблонів
# - get_queryset(), повертає queryset для списку/об’єкта
# - get_object(), повертає один об’єкт (за pk/slug)
# - get_form(), повертає екземпляр форми
# - get_form_class(), повертає клас форми
# - get_success_url(), куди редіректити після успішної дії

#######################################################################################################
# також є можливість створювати синхронні та асинхронні ListView, DetailView та інші,
# але це вже трохи складніше і зазвичай потребує додаткової обробки даних моделей

class CityListView(ListView):
    """
    Асинхронний класовий вигляд ListView без використання моделі.
    Просто передаємо статичний список міст у шаблон.
    """
    template_name = "weather/city_list.html"  # шлях до шаблону
    context_object_name = "cities"  # ім'я змінної в шаблоні

    # статичний список міст (потім можна буде замінити на дані моделі)
    cities_data = [
        {"name": "Одеса", "population": 1010000, "region": "Одеська область"},
        {"name": "Київ", "population": 2960000, "region": "Київська область"},
        {"name": "Львів", "population": 717000, "region": "Львівська область"},
        {"name": "Харків", "population": 1419000, "region": "Харківська область"},
        {"name": "Дніпро", "population": 980000, "region": "Дніпропетровська область"},
    ]

    def get_queryset(self):
        """
        ListView очікує queryset, але повертається просто список словників.
        """
        return self.cities_data

    async def get_context_data(self, **kwargs):
        """
        Асинхронна функція - додаємо додаткові дані в контекст
        """
        context = await sync_to_async(super().get_context_data)(**kwargs)
        # імітація асинхронної операції (наприклад, запит до БД)
        await asyncio.sleep(0.1)
        context["updated_at"] = time.strftime("%H:%M:%S")
        context["total_cities"] = len(self.cities_data)
        return context

    async def get(self, request, *args, **kwargs):
        """Асинхронний GET метод"""
        self.object_list = self.get_queryset()
        context = await self.get_context_data(**kwargs)
        return await sync_to_async(self.render_to_response)(context)
