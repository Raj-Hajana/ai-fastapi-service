import os
import time
from typing import Dict, Any
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(
    title="AI Inference Service",
    description="A lightweight AI microservice for text analysis and sentiment classification",
    version="1.0.0"
)

# Simulated AI Model State
MODEL_NAME = os.getenv("MODEL_NAME", "distilbert-sentiment-v1")
MODEL_VERSION = os.getenv("MODEL_VERSION", "1.0.0")
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))

class TextAnalysisRequest(BaseModel):
    text: str

class TextAnalysisResponse(BaseModel):
    model: str
    version: str
    tokens_count: int
    sentiment: str
    confidence: float
    latency_ms: float

@app.get("/", tags=["Root"])
def read_root() -> Dict[str, str]:
    return {
        "message": "AI Inference Service is running",
        "docs_url": "/docs",
        "health_check": "/health"
    }

@app.get("/health", tags=["Monitoring"])
def health_check() -> Dict[str, Any]:
    return {
        "status": "healthy",
        "service": "ai-fastapi-service",
        "model": MODEL_NAME,
        "version": MODEL_VERSION
    }

@app.post("/v1/analyze", response_model=TextAnalysisResponse, tags=["AI Inference"])
def analyze_text(payload: TextAnalysisRequest) -> TextAnalysisResponse:
    start_time = time.time()
    
    if not payload.text.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Input text cannot be empty."
        )

    # Lightweight deterministic simulation of an NLP sentiment classification model
    tokens = payload.text.split()
    token_count = len(tokens)
    
    # Simple heuristic for dummy sentiment
    lowered = payload.text.lower()
    positive_words = {"good", "great", "excellent", "fast", "love", "awesome", "reliable", "scalable"}
    negative_words = {"bad", "slow", "error", "fail", "broken", "terrible", "downtime", "bug"}
    
    pos_score = sum(1 for w in tokens if w.lower().strip(".,!?:;") in positive_words)
    neg_score = sum(1 for w in tokens if w.lower().strip(".,!?:;") in negative_words)
    
    if pos_score > neg_score:
        sentiment = "POSITIVE"
        confidence = min(0.98, 0.65 + (pos_score * 0.08))
    elif neg_score > pos_score:
        sentiment = "NEGATIVE"
        confidence = min(0.95, 0.60 + (neg_score * 0.08))
    else:
        sentiment = "NEUTRAL"
        confidence = 0.50

    latency_ms = round((time.time() - start_time) * 1000 + 12.5, 2)

    return TextAnalysisResponse(
        model=MODEL_NAME,
        version=MODEL_VERSION,
        tokens_count=token_count,
        sentiment=sentiment,
        confidence=confidence,
        latency_ms=latency_ms
    )

@app.get("/v1/cache-stats", tags=["Cache"])
def cache_stats() -> Dict[str, Any]:
    """
    Endpoint to retrieve Redis caching statistics.
    """
    try:
        import redis
        client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, socket_connect_timeout=2)
        client.ping()
        client.incr("api:request_count")
        count = int(client.get("api:request_count") or 0)
        return {
            "status": "connected",
            "redis_host": REDIS_HOST,
            "redis_port": REDIS_PORT,
            "total_cached_requests": count
        }
    except Exception as exc:
        return {
            "status": "disconnected",
            "redis_host": REDIS_HOST,
            "redis_port": REDIS_PORT,
            "error": str(exc),
            "hint": "Check docker-compose networking or verify Redis container is running."
        }

if __name__ == "__main__":
    import uvicorn
    # Default binding to 0.0.0.0 for container compatibility
    host = os.getenv("APP_HOST", "0.0.0.0")
    port = int(os.getenv("APP_PORT", "8000"))
    uvicorn.run("main:app", host=host, port=port, reload=True)
