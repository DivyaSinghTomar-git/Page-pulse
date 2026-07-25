# Technology Decision Record (TDR)

## 1. FastAPI

### Selected
FastAPI was chosen because it provides high performance, automatic request validation using Pydantic, asynchronous support, and built-in Swagger documentation.

### Alternative Considered
Flask

### Why Rejected
Flask requires additional libraries for validation and API documentation, resulting in more boilerplate code.

---

## 2. HTTPX

### Selected
HTTPX supports asynchronous HTTP requests, making it suitable for auditing multiple URLs efficiently.

### Alternative Considered
Requests

### Why Rejected
Requests is synchronous and less suitable for high-concurrency applications.

---

## 3. SlowAPI

### Selected
SlowAPI provides easy-to-configure rate limiting for FastAPI applications.

### Alternative Considered
Custom middleware

### Why Rejected
A custom implementation would increase complexity and maintenance effort.

---

## 4. In-Memory Cache

### Selected
An in-memory cache was chosen because it is lightweight and sufficient for this assignment.

### Alternative Considered
Redis

### Why Rejected
Redis introduces additional infrastructure. For a lightweight assignment, an in-memory cache is simpler while demonstrating the same caching concept.

---

## 5. GitHub Actions

### Selected
GitHub Actions was chosen to automatically execute tests on every push.

### Alternative Considered
Jenkins

### Why Rejected
Jenkins requires separate infrastructure and configuration, while GitHub Actions integrates directly with the repository.