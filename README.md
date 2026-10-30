# Issue: Service Unreachable on Host Port 8000

### Description
The container starts up successfully and `docker ps` indicates that port `8000` is forwarded.
However, sending a request to the health endpoint fails:

```bash
docker build -t ai-service .
docker run -d -p 8000:8000 --name ai-app ai-service
curl http://localhost:8000/health
```

**Symptom**:
`curl: (56) Recv failure: Connection reset by peer` or `Failed to connect to localhost port 8000`.

---

### Task
1. Inspect the container logs and runtime behavior using Docker commands (`docker ps`, `docker logs`, etc.).
2. Identify why traffic from the host machine cannot reach the application inside the container.
3. Fix the issue, rebuild, and verify that `curl http://localhost:8000/health` returns `200 OK`.
