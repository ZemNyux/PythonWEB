from django.urls import path
from . import views

urlpatterns = [
    path('', views.branches_list, name='branches_list'),
    path('Odesa/', views.odesa, name='odesa'), 
    path('Orleans/', views.orleans, name='orleans'),
]