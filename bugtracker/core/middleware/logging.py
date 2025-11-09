import logging

request_logger = logging.getLogger('system_logger')

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, req):
        ip = req.META.get('REMOTE_ADDR')
        agent = req.META.get('HTTP_USER_AGENT', 'unknown')
        path = req.path

        request_logger.info(f"Request: IP={ip}, PATH={path}, AGENT={agent}")

        return self.get_response(req)
