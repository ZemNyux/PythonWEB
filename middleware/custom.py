import time
def log_requests(get_response):
    """Логує кожен запит: метод, шлях, час виконання, статус відповіді"""

    def middleware(request):
        start_time = time.time()

        response = get_response(request)

        duration = time.time() - start_time
        status = response.status_code

        print(f"[{status}] {request.method} {request.path} — {duration:.3f} секунд. Привіт із мідлварі!")

        return response

    return middleware

class CustomHeaderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        response['X-Powered-By'] = 'ZemNyux 26/02/2026'
        response['X-Company-Name'] = 'ZemNyux Inc.'

        return response
