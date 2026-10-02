# Production Deployment Guide

## 1. Local / On-Premise Execution
Run the full orchestration runner:
```bash
python run_full_system.py
```
Frontend & API will be available at `http://127.0.0.1:8000`.

## 2. Docker Container Deployment
Build and run the container:
```bash
docker build -t mindtrack-ai -f 08_deployment_configuration/Dockerfile .
docker run -p 8000:8000 mindtrack-ai
```

Or using Docker Compose:
```bash
docker-compose -f 08_deployment_configuration/docker-compose.yml up --build
```

## 3. Cloud Platforms (Render / Railway / Heroku)
1. Push repository to GitHub.
2. Link the repository to Render (Web Service) using `render.yaml` or Heroku using `Procfile`.
3. Set environment variable `PORT=8000` (or leave default assigned by platform).
