from django.urls import path
from . import views

urlpatterns = [
    path('', views.branches_list, name='branches_list'),
    path('London/', views.london, name='london'),
    path('Paris/', views.paris, name='paris'),
    # Розділ History та його підрозділи
    path('history/', views.history_main, name='history_main'),
    path('history/dates/', views.history_dates, name='history_dates'),
    path('history/facts/', views.history_facts, name='history_facts'),
]