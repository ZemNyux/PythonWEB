from django.urls import path, re_path
from core import views

urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^news/.*$', views.news, name='news'),
    re_path(r'^management/.*$', views.management, name='management'),
    re_path(r'^about/.*$', views.about, name='about'),
    re_path(r'^contacts/(?P<country>[\w-]+)?/?$', views.contacts, name='contacts'),
]