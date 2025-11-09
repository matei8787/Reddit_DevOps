from django.utils.deprecation import MiddlewareMixin

class SecurityHeadersMiddleware(MiddlewareMixin):
    def process_response(self, req, res):
        res["X-Content-Type-Options"] = "nosniff"
        res["X-Frame-Options"] = "DENY"
        res["X-XSS-Protection"] = "1; mode=block"
        res["Referrer-Policy"] = "strict-origin-when-cross-origin"
        return res
