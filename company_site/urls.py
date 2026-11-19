from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('history/', RedirectView.as_view(url='/branches/history/', permanent=False)),
    path('branch/', RedirectView.as_view(url='/branches/', permanent=False)),
    path('contact/', RedirectView.as_view(url='/contacts/', permanent=False)),

    path('', include('core.urls')),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()

handler404 = 'core.views.custom_404_view'
