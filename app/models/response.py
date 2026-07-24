from pydantic import BaseModel


class AuditResponse(BaseModel):
    url: str
    status_code: int
    response_time_ms: float
    success: bool
    from_cache: bool
    message: str