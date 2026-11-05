from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                           # головна сторінка
    path('json/', views.json_response, name='json-response'),    # JsonResponse
    path('redirect/', views.redirect_example, name='redirect'),  # HttpResponseRedirect
    path('file/', views.file_response, name='file-response'),    # FileResponse
    path('stream/', views.streaming_response, name='streaming'), # StreamingHttpResponse
]