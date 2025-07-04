# Task API – FastAPI Microservice

A simple RESTful API built with FastAPI to manage tasks with JWT authentication.

## Features
- Login with username/password to get JWT token
- Protected endpoints (CRUD operations on tasks)
- SQLite for persistence
- Pydantic validation

## Run

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## Endpoints

- `POST /token` – Get JWT token (username: admin, password: admin)
- `POST /tasks/` – Create task (token required)
- `GET /tasks/` – List tasks (token required)
