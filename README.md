# Issue: Container Exits Immediately on Startup

### Description
The application image builds, but when running the container in detached mode:

```bash
docker build -t ai-service .
docker run -d -p 8000:8000 --name ai-app ai-service
```

Running `docker ps` returns an empty list. The container terminated immediately after launching.

---

### Task
1. Use Docker diagnostic commands (`docker ps -a`, `docker logs`, etc.) to find the stopped container and read its exit code and error logs.
2. Identify why the application failed to start inside the container.
3. Fix the issue, rebuild, and verify that the container stays up and responds at `curl http://localhost:8000/health`.
