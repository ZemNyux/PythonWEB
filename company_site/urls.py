from core import views
from django.urls import path, re_path

urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^news/.*$', views.news, name='news'),
    re_path(r'^management/.*$', views.management, name='management'),
    re_path(r'^about/.*$', views.about, name='about'),
    re_path(r'^contacts/.*$', views.contacts, name='contacts'),
]