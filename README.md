# AI FastAPI Service

A lightweight microservice built with FastAPI providing simulated text analysis and sentiment classification, along with Redis caching support.

---

## Features
- **Health Check**: `GET /health` endpoint for readiness and liveness status.
- **Text Analysis**: `POST /v1/analyze` for sentiment classification and token latency metrics.
- **Cache Statistics**: `GET /v1/cache-stats` for checking Redis connectivity and cached request counts.
- **OpenAPI Documentation**: Automatically generated interactive Swagger and ReDoc interfaces.

---

## Getting Started

### Prerequisites
- Python 3.10+
- `pip`

### 1. Setup Virtual Environment
```bash
# Clone the repository
git clone https://github.com/Raj-Hajana/ai-fastapi-service.git
cd ai-fastapi-service

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate
# On Linux/macOS:
source .venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Service Locally
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

Once running, interactive documentation is available at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

---

## API Endpoints

### 1. Health Check
```bash
curl http://localhost:8000/health
```

**Response (`200 OK`)**:
```json
{
  "status": "healthy",
  "service": "ai-fastapi-service",
  "model": "distilbert-sentiment-v1",
  "version": "1.0.0"
}
```

### 2. Analyze Text
```bash
curl -X POST http://localhost:8000/v1/analyze \
  -H "Content-Type: application/json" \
  -d "{\"text\": \"This service is fast, reliable, and scalable!\"}"
```

**Response (`200 OK`)**:
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
```bash
curl http://localhost:8000/v1/cache-stats
```

---

## Configuration

Environment variables can be configured via terminal or `.env` file:

| Variable | Default | Description |
| :--- | :--- | :--- |
| `APP_HOST` | `0.0.0.0` | Host address to bind the web server |
| `APP_PORT` | `8000` | Port for incoming HTTP requests |
| `MODEL_NAME` | `distilbert-sentiment-v1` | Identifier for simulated inference model |
| `MODEL_VERSION` | `1.0.0` | Model version tag |
| `REDIS_HOST` | `localhost` | Hostname for Redis caching service |
| `REDIS_PORT` | `6379` | Port for Redis caching service |
