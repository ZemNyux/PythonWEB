from branches import views as branches_views  # Импортируем вьюхи из branches
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    # Подключаем остальные разделы (home, about и т.д. из core или company_site)
    # ... твои текущие пути ...

    # Добавляем маршруты для истории прямо в корень, как требует практика:
    path('history/', branches_views.history_main, name='history_main'),
    path('history/dates/', branches_views.history_dates, name='history_dates'),
    path('history/facts/', branches_views.history_facts, name='history_facts'),

    # И приложение branches если нужно:
    path('branches/', include('branches.urls')),
]