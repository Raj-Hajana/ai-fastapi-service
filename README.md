# AI FastAPI Service - DevOps Interview Assessment

A lightweight microservice built with FastAPI providing simulated text analysis and sentiment classification, along with Redis caching support.

---

## Candidate Assessment Overview

Welcome to the technical assessment! In this interview, you will demonstrate hands-on proficiency in local application setup, containerization with Docker, and real-world troubleshooting.

### Assessment Tasks:

1. **Clone & Local Execution**
   - Clone the repository to your local environment.
   - Set up the environment, resolve dependencies, and execute the service locally.
   - Verify that the application is running properly and test the endpoints.

2. **Containerization (Docker)**
   - Create a `Dockerfile` to containerize the FastAPI service following container best practices.
   - Build the Docker image and run the application container.
   - Ensure the containerized service is reachable on the host machine.
   - *(Optional / Multi-Container)*: Orchestrate the service alongside a Redis instance (e.g., using Docker Compose) to enable the caching endpoints.

3. **Troubleshooting & Bug Fixing (2 Scenarios)**
   - You will be assigned 2 troubleshooting scenarios / bug branches during the assessment.
   - Inspect container and system logs, diagnose root causes (such as networking, binding, dependency, or port issues), and implement the fixes.
   - Re-test and verify that the application and endpoints function correctly.

---

## Features
- **Health Check**: `GET /health` endpoint for readiness and liveness status.
- **Text Analysis**: `POST /v1/analyze` for sentiment classification and token latency metrics.
- **Cache Statistics**: `GET /v1/cache-stats` for checking Redis connectivity and cached request counts.
- **OpenAPI Documentation**: Automatically generated interactive Swagger and ReDoc interfaces.

---

## Technical Specifications

### Requirements
- Python 3.10+
- Dependencies defined in `requirements.txt`
- Redis (for caching features)

### Application Entrypoint
- FastAPI application instance: `app.main:app`
- Interactive documentation:
  - Swagger UI: `/docs`
  - ReDoc: `/redoc`

---

## API Specification

### 1. Health Check
- **Method & Path**: `GET /health`
- **Description**: Readiness and liveness status probe.
- **Response (`200 OK`)**:
```json
{
  "status": "healthy",
  "service": "ai-fastapi-service",
  "model": "distilbert-sentiment-v1",
  "version": "1.0.0"
}
```

### 2. Analyze Text
- **Method & Path**: `POST /v1/analyze`
- **Description**: Performs text analysis and sentiment classification.
- **Request Body (`application/json`)**:
```json
{
  "text": "This service is fast, reliable, and scalable!"
}
```
- **Response (`200 OK`)**:
```json
{
  "model": "distilbert-sentiment-v1",
  "version": "1.0.0",
  "tokens_count": 8,
  "sentiment": "POSITIVE",
  "confidence": 0.89,
  "latency_ms": 13.2
}
```

### 3. Cache Stats (Redis)
- **Method & Path**: `GET /v1/cache-stats`
- **Description**: Verifies Redis connectivity and retrieves cached request statistics.

---

## Configuration

Environment variables can be configured via environment settings or a `.env` file:

| Variable | Default | Description |
| :--- | :--- | :--- |
| `APP_HOST` | `0.0.0.0` | Host address to bind the web server |
| `APP_PORT` | `8000` | Port for incoming HTTP requests |
| `MODEL_NAME` | `distilbert-sentiment-v1` | Identifier for simulated inference model |
| `MODEL_VERSION` | `1.0.0` | Model version tag |
| `REDIS_HOST` | `localhost` | Hostname for Redis caching service |
| `REDIS_PORT` | `6379` | Port for Redis caching service |

