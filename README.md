# Issue: Redis Connection Failure in Docker Compose

### Description
The multi-container stack is launched using Docker Compose:

```bash
docker compose up -d --build
```

Both containers appear as running in `docker compose ps`.
However, testing the cache statistics endpoint:

```bash
curl http://localhost:8000/v1/cache-stats
```

Returns:
```json
{
  "status": "disconnected",
  "error": "Error connecting to localhost:6379. Connection refused.",
  "hint": "Check docker-compose networking or verify Redis container is running."
}
```

---

### Task
1. Inspect the running containers and network configuration with Docker CLI tools.
2. Determine why the API container cannot reach the Redis container using `localhost`.
3. Update `docker-compose.yml`, restart the stack, and verify that `curl http://localhost:8000/v1/cache-stats` returns `"status": "connected"`.
