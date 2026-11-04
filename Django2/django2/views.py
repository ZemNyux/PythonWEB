from datetime import datetime
from django.http import HttpResponse


def time_view(request):
    html = """
    <body>
        <h1>Поточний час</h1>
        <div id="clock"></div>
        <script>
            function updateTime() {
                const now = new Date();
                document.getElementById('clock').innerText = now.toLocaleTimeString() + '.' + String(now.getMilliseconds()).padStart(3, '0');
            }
            setInterval(updateTime, 1);
        </script>
        <br><br>
        <a href="/date/">Перейти до поточної дати</a>
    </body>
    """
    return HttpResponse(html)


def date_view(request):
    current_date = datetime.now().strftime("%d.%m.%Y")
    html = f"""
    <body>
        <h1>Поточна дата</h1>
        <p>{current_date}</p>
        <br><br>
        <a href="/time/">Перейти до поточного часу</a>
    </body>
    """
    return HttpResponse(html)