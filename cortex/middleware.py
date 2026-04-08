from starlette.middleware.base import BaseHTTPMiddleware
from utils.logging import log

class RequestLogger(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        log(f"{request.method} {request.url.path}")
        response = await call_next(request)
        return response
