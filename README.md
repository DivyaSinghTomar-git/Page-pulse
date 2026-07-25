# 🚀 Page Pulse

A production-ready URL Audit Service built using **FastAPI** for the **Digital Heroes Software Development Assignment**.

## Live Demo

https://page-pulse-mn9n.onrender.com

## GitHub Repository

https://github.com/DivyaSinghTomar-git/Page-pulse

---

## Features

- URL validation using Pydantic
- URL audit using HTTPX
- Configurable request timeout
- Concurrency control using asyncio Semaphore
- In-memory caching
- Rate limiting per client
- Structured logging
- Request ID middleware
- Structured error handling
- Unit testing with Pytest
- CI using GitHub Actions
- FastAPI Swagger Documentation

---

## API Endpoints

### Health Check

**GET /**

Response

```json
{
  "message": "Page Pulse API Running",
  "credits": "Built for Digital Heroes Training Task"
}
```

---

### Audit URL

**POST /audit**

Request

```json
{
  "url": "https://google.com"
}
```

Successful Response

```json
{
  "url": "https://google.com/",
  "status_code": 200,
  "response_time_ms": 698.74,
  "success": true,
  "from_cache": false,
  "message": "Audit completed successfully"
}
```

---

## API Documentation

Swagger UI

https://page-pulse-mn9n.onrender.com/docs

---

## Installation

```bash
git clone https://github.com/DivyaSinghTomar-git/Page-pulse.git

cd Page-pulse

pip install -r requirements.txt
```

Run locally

```bash
uvicorn app.main:app --reload
```

---

## Running Tests

```bash
python -m pytest
```

---

## Tech Stack

- Python 3.12
- FastAPI
- HTTPX
- SlowAPI
- Pytest
- GitHub Actions
- Render

---

## Project Structure

```
app/
 ├── api
 ├── cache
 ├── middleware
 ├── models
 ├── services
 ├── utils

tests/

.github/workflows/
```

---

## Author

Divya Singh Tomar
