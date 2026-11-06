from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Переадресація для поширених скорочень або альтернативних адрес
    path('history/', RedirectView.as_view(url='/branches/history/', permanent=False)),
    path('branch/', RedirectView.as_view(url='/branches/', permanent=False)),
    path('contact/', RedirectView.as_view(url='/contacts/', permanent=False)),

    # Основний маршрутизатор
    path('', include('core.urls')),
]

# Роздача статичних файлів у режимі розробки
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()

# Кастомна сторінка 404 помилки
handler404 = 'core.views.custom_404_view'
