from django.urls import include, path, re_path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('news/', views.news, name='news'),
    re_path(r'^news/.+', views.news),
    path('management/', views.management, name='management'),
    re_path(r'^management/.+', views.management),
    path('about/', views.about, name='about'),
    re_path(r'^about/.+', views.about),
    path('contacts/', views.contacts, name='contacts'),
    path('contacts/<slug:country>/', views.contacts, name='contacts_country'),
    path('branches/', include('branches.urls')),
]
