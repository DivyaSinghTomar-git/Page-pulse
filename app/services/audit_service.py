import asyncio
import time

import httpx
from fastapi import HTTPException

from app.cache.cache_service import get_cached, set_cache

CACHE_TTL = 60  # seconds

MAX_CONCURRENT_REQUESTS = 20
semaphore = asyncio.Semaphore(MAX_CONCURRENT_REQUESTS)


async def audit_url(url: str):

    # Check cache first
    cached_response = get_cached(url)

    if cached_response:
        cached_response["from_cache"] = True
        return cached_response

    start = time.perf_counter()

    try:
        async with semaphore:
            async with httpx.AsyncClient(
                timeout=10,
                follow_redirects=True
            ) as client:

                response = await client.get(url)

        elapsed = round((time.perf_counter() - start) * 1000, 2)

        result = {
            "url": url,
            "status_code": response.status_code,
            "response_time_ms": elapsed,
            "success": True,
            "from_cache": False,
            "message": "Audit completed successfully"
        }

        # Save to cache
        set_cache(url, result, CACHE_TTL)

        return result

    except httpx.TimeoutException:
        raise HTTPException(
            status_code=408,
            detail="Request to target URL timed out."
        )

    except httpx.RequestError:
        raise HTTPException(
            status_code=502,
            detail="Unable to connect to target URL."
        )