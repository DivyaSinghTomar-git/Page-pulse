from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from slowapi import _rate_limit_exceeded_handler

from app.limiter import limiter
from fastapi import FastAPI

from app.api.routes import router

from app.middleware.request_id import RequestIDMiddleware
from app.middleware.logging import LoggingMiddleware

app = FastAPI(
    title="Page Pulse",
    version="1.0.0",
    description="URL Audit Service for Digital Heroes"
)

# Middleware (order matters)

app.add_middleware(LoggingMiddleware)
app.add_middleware(RequestIDMiddleware)
app.add_middleware(SlowAPIMiddleware)

app.include_router(router)


@app.get("/")
async def root():
    return {
        "message": "Page Pulse API Running",
        "credits": "Built for Digital Heroes Training Task"
    }
app.state.limiter = limiter

app.add_exception_handler(
    RateLimitExceeded,
    _rate_limit_exceeded_handler
)