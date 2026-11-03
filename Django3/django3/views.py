from django.http.response import HttpResponse

def main_page(request):
    # return render(request, 'main.html')
    return HttpResponse("<h1>Головна сторінка першого додатку</h1>")


def second_page(request):
    # return render(request, 'second.html')
    return HttpResponse("<h1>Другий розділ першого додатку</h1>")


def weather_odesa(request):
    # return render(request, 'weather.html')
    return HttpResponse("<h1>Третій розділ першого додатку</h1>")