import time
import traceback
from starlette.middleware.base import BaseHTTPMiddleware


class LoggingMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request, call_next):
        try:
            print("Logging middleware started")

            start = time.time()

            response = await call_next(request)

            duration = round((time.time() - start) * 1000, 2)

            print(
                f"Request ID: {getattr(request.state, 'request_id', 'NOT FOUND')}"
            )
            print(
                f"{request.method} {request.url.path} "
                f"{response.status_code} {duration} ms"
            )

            return response

        except Exception:
            traceback.print_exc()
            raise