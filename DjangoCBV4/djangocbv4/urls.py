from django.contrib import admin
from django.urls import include, path  # Не забудь импортировать include

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        '', include('weather.urls')
    ),  # Подключаем маршруты приложения weather в корень
]