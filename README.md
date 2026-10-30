# Issue: Container Port Mismatch

### Description
The container was built and launched with the standard port mapping:

```bash
docker build -t ai-service .
docker run -d -p 8000:8000 --name ai-app ai-service
```

`docker ps` indicates the container is up and running.
However, attempting to access the service from the host machine fails:

```bash
curl http://localhost:8000/health
```

**Symptom**:
`curl: (7) Failed to connect to localhost port 8000: Connection refused` (or `Connection reset by peer`).

---

### Task
1. Inspect the container runtime logs and environment using Docker CLI tools (`docker logs`, `docker inspect`, etc.).
2. Determine which port the internal web service is actually listening on.
3. Resolve the port mismatch so that the service is accessible on host port `8000`.
4. Verify that `curl http://localhost:8000/health` returns `200 OK`.
