company_site / core / urls.py:
  
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),
    path('news/', views.news, name='news'),
    path('management/', views.management, name='management'),

    # path('about/', views.about, name='about'),
    ######################################################################
    path('about/', TemplateView.as_view(
        template_name='about.html',
        extra_context={'title': 'Про компанію Versailles Cortège'}
    ), name='about'),
    ######################################################################

    path('contacts/', views.contacts, name='contacts'),

    # URL для розділу "Філії" (він підключає branches/urls.py)
    path('branches/', include('branches.urls')),
]

==============================================================================================

company_site / core / views.py:

from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {'title': 'Головна'})

def news(request):
    return render(request, 'news.html', {'title': 'Новини'})

def management(request):
    return render(request, 'management.html', {'title': 'Керівництво компанії'})

# функції about у views.py вже не потрібно
# def about(request):
#     return render(request, 'about.html', {'title': 'Про компанію'})

def contacts(request):
    return render(request, 'contacts.html', {'title': 'Контакти'})