# Architecture Document

## Overview

Page Pulse is a production-ready URL auditing service built using FastAPI. It accepts a URL from the client, validates the request, audits the target website by making an HTTP request, and returns details such as HTTP status code, response time, and success status.

To improve performance and reliability, the application includes in-memory caching, request rate limiting, request ID tracking, structured logging, timeout handling, and concurrency control.

---

## Components

### Client

Any HTTP client (Swagger UI, Postman, browser, or application) sends requests to the API.

### FastAPI Application

Receives incoming HTTP requests and routes them to the appropriate endpoint.

### Middleware

- Request ID Middleware
- Logging Middleware
- SlowAPI Rate Limiting Middleware

These provide request tracing, structured logging, and client protection.

### API Router

Handles endpoint routing.

### Audit Service

Contains the business logic.

Responsibilities:

- Validate input
- Check cache
- Fetch remote URL
- Measure response time
- Handle timeout/errors
- Return structured response

### Memory Cache

Stores recently audited URLs for a configurable time window to reduce repeated external requests.

### HTTP Client (HTTPX)

Performs outbound requests to target websites.

---

## Data Flow

1. Client sends POST /audit request.
2. FastAPI validates the request.
3. Middleware generates Request ID.
4. Rate limiter checks client limits.
5. Audit Service checks cache.
6. If cached, cached response is returned.
7. Otherwise HTTPX fetches the target URL.
8. Response is processed and cached.
9. JSON response is returned to the client.

---

## Queueing Strategy

Current implementation controls concurrent outbound requests using an asyncio Semaphore.

If traffic increases significantly (thousands of concurrent requests), the architecture can be extended by introducing a distributed task queue such as Celery with Redis.

---

## State Management

Current state consists of:

- In-memory cache
- Request context
- Application configuration

The service remains stateless apart from the cache, making horizontal scaling straightforward by replacing the cache with Redis.