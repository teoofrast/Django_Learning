import logging

logger = logging.getLogger()


class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        # Логируем начало запроса
        logger.warning(f"Request: {request.method}, Path: {request.path}, User: {request.user}")
        response = self.get_response(request)

        # Логируем завершение запроса
        logger.warning(f"Response: {response.status_code}")

        return response
