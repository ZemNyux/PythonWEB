from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path('', views.branches_list, name='branches_list'),
    path('history/', views.history_main, name='history_main'),
    path('history/dates/', views.history_dates, name='history_dates'),
    path('history/facts/', views.history_facts, name='history_facts'),
    path('London/', RedirectView.as_view(url='/branches/london/', permanent=False)),
    path('Paris/', RedirectView.as_view(url='/branches/paris/', permanent=False)),
    path('Berlin/', RedirectView.as_view(url='/branches/berlin/', permanent=False)),
    path('<slug:slug>/', views.branch_detail, name='branch_detail'),
]
