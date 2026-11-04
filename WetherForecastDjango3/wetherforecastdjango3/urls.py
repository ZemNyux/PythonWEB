from django.urls import path
from django.views.generic import RedirectView  # Импортируем редирект
from .views import main_page, second_page, weather_odesa

urlpatterns = [
    path("", RedirectView.as_view(url="/weather/")),  # <--- Теперь корень сразу кидает на погоду!
    path("home/", main_page, name="main"),  # Старую главную можно перенести сюда
    path("second/", second_page, name="second"),
    path("weather/", weather_odesa, name="weather"),
]