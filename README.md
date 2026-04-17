# FastAPI API Key & Rate Limiting Service

## Overview

This project implements a backend service using FastAPI that provides:

- API key generation
- Secure access to protected endpoints
- Rate limiting per API key
- Basic usage tracking

The system is designed with a modular architecture using FastAPI best practices such as dependency injection and Pydantic models.

---

## Features

- Generate API keys via `/keys`
- Authenticate requests using `X-API-Key` header
- Protect endpoints using dependency-based authentication
- Rate limiting (5 requests per minute per API key)
- Usage tracking per API key
- Interactive API documentation using Swagger (`/docs`)

---

## Project Structure

```
app/
  api/
    routes/
    deps.py
  core/
  db/
  models/
  schemas/
  services/
  utils/
```

---

## Setup Instructions

```bash
git clone https://github.com/your-username/fastapi-api-key-service.git
cd fastapi-api-key-service

python -m venv venv
venv\Scripts\activate   # Windows

pip install -r requirements.txt
```

---

## Run the Application

```bash
uvicorn app.main:app --reload
```

---

## API Documentation

Swagger UI is available at:

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## Endpoints

### 1. Generate API Key

POST /keys

Response:

```json
{
  "key": "your_api_key",
  "created_at": "timestamp"
}
```

---

### 2. Protected Route

GET /protected

Requires header:

X-API-Key: your_api_key

---

### 3. Profile Route

GET /profile

Requires authentication via API key.

---

## Rate Limiting

- Limit: 5 requests per 60 seconds per API key
- Exceeding limit returns:

```json
{
  "detail": "Rate limit exceeded"
}
```

HTTP Status: 429 Too Many Requests

---

## Postman Collection

The Postman collection is included in the repository:

postman_collection.json

It can be imported directly into Postman for testing all endpoints.

---

## Assumptions & Design Decisions

- In-memory storage is used for API keys and request tracking
- Rate limiting is implemented using a fixed time window approach
- No external database (e.g., PostgreSQL, Redis) is used to keep the solution simple
- API key validation is handled using FastAPI dependency injection
- The architecture is modular to allow easy extension (e.g., adding database or Redis later)

---

## Notes

- Data will reset on server restart due to in-memory storage
- Designed for demonstration and learning purposes, not producti
