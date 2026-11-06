from django.urls import path
from . import views

urlpatterns = [
    path('', views.branches_list, name='branches_list'),
    path('london/', views.london, name='london'),
    path('London/', views.london),
    path('paris/', views.paris, name='paris'),
    path('Paris/', views.paris),
    path('berlin/', views.berlin, name='berlin'),
    path('Berlin/', views.berlin),
    # Розділ History та його підрозділи
    path('history/', views.history_main, name='history_main'),
    path('history/dates/', views.history_dates, name='history_dates'),
    path('history/facts/', views.history_facts, name='history_facts'),
]
