from django.http import (
    HttpResponse,
    JsonResponse,
    HttpResponseRedirect,
    FileResponse,
    StreamingHttpResponse,
)
from django.shortcuts import render
import os
import time


def home(request):
    """Головна сторінка з посиланнями на всі приклади"""
    return render(request, 'weather.html')


def json_response(request):
    """Приклад JsonResponse"""
    data = {
        "status": "success",
        "message": "Це JSON-відповідь від Django",
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "request_method": request.method,
        "query_params": dict(request.GET),
    }
    return JsonResponse(data, status=200)


def redirect_example(request):
    """Приклад HttpResponseRedirect"""
    # наприклад, після успішної відправки даних форми - редірект на головну
    return HttpResponseRedirect('/')


def file_response(request):
    """Приклад FileResponse — віддача файлу (наприклад, PDF або зображення)"""
    # !!! шлях до файлу — ТРЕБА ЗАМІНИТИ на реальний файл !!!
    file_path = r"C:\!Files\pdf\ipresentation.pdf"  # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< !!!

    if not os.path.exists(file_path):
        return HttpResponse("Файл не знайдено", status=404)

    # віддаємо файл з правильним ім'ям і типом
    response = FileResponse(
        open(file_path, 'rb'),
        as_attachment=True,  # завантажити як файл
        filename="my_document.pdf",  # ім'я файлу для користувача
        content_type="application/pdf"
    )
    return response


def streaming_response(request):
    """Приклад StreamingHttpResponse — потокова передача (великі файли, генерація на льоту)"""

    def generate_large_content():
        """Імітація створення великого контенту"""
        yield "Початок потоку...\n"
        for i in range(1, 21):
            time.sleep(0.3)  # імітація довгої роботи
            yield f"Частина {i} з 20\n"
        yield "Кінець потоку!"

    response = StreamingHttpResponse(
        generate_large_content(),
        content_type="text/plain"
    )
    response['Content-Disposition'] = 'attachment; filename="stream.txt"'
    return response
