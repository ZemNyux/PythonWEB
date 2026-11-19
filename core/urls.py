from django.urls import include, path, re_path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('news/', views.news, name='news'),
    re_path(r'^news/.+$', RedirectView.as_view(url='/news/', permanent=False)),
    path('management/', views.management, name='management'),
    re_path(r'^management/.+$', RedirectView.as_view(url='/management/', permanent=False)),
    path('about/', views.about, name='about'),
    re_path(r'^about/.+$', RedirectView.as_view(url='/about/', permanent=False)),
    path('contacts/', views.contacts, name='contacts'),
    path('contacts/<slug:country>/', views.contacts, name='contacts_country'),
    path('branches/', include('branches.urls')),
]
