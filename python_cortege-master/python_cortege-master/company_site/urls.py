from django.conf import settings
from django.shortcuts import render
from django.urls import path, include
from django.conf.urls.static import static
from django.views import defaults as default_views

urlpatterns = [
    path('', include('core.urls')),
    
    path('404/', default_views.page_not_found),
    path('403/', default_views.permission_denied), 
    path('500/', default_views.server_error),
    # авторизації поки що нема, тому для демо 403 помилка буде викликатися через окремий URL
    path('demo-403/', lambda request: render(request, '403.html', status=403), name='demo-403'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)