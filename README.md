# CI/CD Pipeline for a Dockerized Flask Application

A beginner DevOps portfolio project: build a small Flask web app, test it with pytest, package it into a Docker image, and automate test/build steps with GitHub Actions.

## Endpoints
- `/` — returns a JSON welcome message
- `/health` — health check endpoint

## Run locally
```bash
python -m venv .venv
# macOS/Linux: source .venv/bin/activate
# Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
python app.py
```
Visit http://localhost:5000 and http://localhost:5000/health.

## Run tests
```bash
pytest -v
```

## Build and run with Docker
```bash
docker build -t devops-demo-app .
docker run -d --name devops-demo -p 5000:5000 devops-demo-app
```
Visit http://localhost:5000/health.

## CI
GitHub Actions runs tests and builds a Docker image on pushes and pull requests to `main`.

## Planned extensions
1. Push image to Docker Hub (GitHub Actions secrets).
2. Provision AWS EC2 with Terraform.
3. Deploy the container on EC2.
4. Add monitoring/logging and deployment rollback practice.
