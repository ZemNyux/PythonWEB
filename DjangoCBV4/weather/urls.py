# NewApp / weather / urls.py:
from django.urls import path

from weather.views import CityListView, HelloAsyncView, HelloSyncView, WeatherAsyncTemplateView

urlpatterns = [
    path('', HelloSyncView.as_view(), name='hello-sync-cbv'),
    path('hello-async/', HelloAsyncView.as_view(), name='hello-async-cbv'),
    path('weather-template/', WeatherAsyncTemplateView.as_view(), name='weather-template'),
    path('cities/', CityListView.as_view(), name='city-list'),

]