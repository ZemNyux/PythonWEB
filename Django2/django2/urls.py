from django.contrib import admin
from django.urls import path
from django2.views import date_view, time_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("time/", time_view),
    path("date/", date_view),
]