from django.urls import path
from . import views

urlpatterns = [
    path('about/bio/', views.bio_view, name='bio'),
    path('about/facts/', views.facts_view, name='facts'),
    path('city/info/', views.city_info_view, name='city_info'),
    path('city/places/', views.city_places_view, name='city_places'),
]