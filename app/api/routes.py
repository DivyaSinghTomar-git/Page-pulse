from fastapi import APIRouter, Request

from app.limiter import limiter

from fastapi import APIRouter

from app.models.request import AuditRequest
from app.models.response import AuditResponse
from app.services.audit_service import audit_url

router = APIRouter()


@router.post("/audit", response_model=AuditResponse)
@limiter.limit("5/minute")
async def audit(request: Request, body: AuditRequest):
    return await audit_url(str(body.url))
