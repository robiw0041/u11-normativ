from django.utils import timezone

class RequestLoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user if request.user.is_authenticated else "AnonymousUser"
        ip = request.META.get('REMOTE_ADDR')
        path = request.path
        time = timezone.now()

        log = f"""
[{time}]
User: {user}
IP: {ip}
Path: {path}
----------------------
"""

        with open('requests.log', 'a') as file:
            file.write(log)

        response = self.get_response(request)
        return response