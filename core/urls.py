from django.urls import include, path, re_path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path('accounts/register/', views.account_register, name='account_register'),
    path('accounts/login/', views.account_login, name='account_login'),
    path('accounts/logout/', views.account_logout, name='account_logout'),
    path('', views.home, name='home'),
    path('news/', views.news, name='news'),
    re_path(r'^news/.+$', RedirectView.as_view(url='/news/', permanent=False)),
    path('management/', views.management, name='management'),
    re_path(r'^management/.+$', RedirectView.as_view(url='/management/', permanent=False)),
    path('about/', views.about, name='about'),
    re_path(r'^about/.+$', RedirectView.as_view(url='/about/', permanent=False)),
    path('contacts/', views.contacts, name='contacts'),
    path('contacts/<slug:country>/', views.contacts, name='contacts_country'),
    path('complaint/', views.product_complaint, name='product_complaint'),
    path('branches/', include('branches.urls')),
]
