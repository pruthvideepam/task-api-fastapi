

# 🧠 Task API – FastAPI Microservice

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-🚀-green?logo=fastapi)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

A lightweight, secure task management API built using **FastAPI**, JWT authentication, and **SQLite** for local persistence.

## ⚙️ Features

- 🔐 Secure login with JWT-based token
- 📥 Create and retrieve tasks
- 💾 SQLite for simplicity and ease of use
- ⚡ Superfast with FastAPI
- 🧪 Interactive Swagger UI for testing


## 🚀 Getting Started

### 🧱 Install Requirements
```bash
pip install -r requirements.txt
````

> Also install:

```bash
pip install python-multipart PyJWT
```

### ▶️ Run the Server

```bash
uvicorn main:app --reload
```

Server will be running at:
👉 `http://127.0.0.1:8000`
Docs: `http://127.0.0.1:8000/docs`

---

## 🔑 Authentication

### 🔐 `POST /token`

**Credentials:**

* `username`: `admin`
* `password`: `admin`

Example using `curl`:

```bash
curl -X POST http://127.0.0.1:8000/token \
  -d "username=admin&password=admin" \
  -H "Content-Type: application/x-www-form-urlencoded"
```

> Returns:

```json
{
  "access_token": "your.jwt.token.here",
  "token_type": "bearer"
}
```

---

## 📦 API Endpoints

### 📝 `POST /tasks/` – Create Task

```json
{
  "title": "Finish Resume",
  "description": "Update resume for Atomic Loops Python Intern"
}
```

Requires Authorization Header:

```http
Authorization: Bearer <your_token>
```

### 📃 `GET /tasks/` – List Tasks

Returns a list of all tasks created by the user.

---

## 🗃 Example Curl Requests

### Create Task:

```bash
curl -X POST http://127.0.0.1:8000/tasks/ \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"title": "Task A", "description": "This is task A"}'
```

### List Tasks:

```bash
curl -X GET http://127.0.0.1:8000/tasks/ \
  -H "Authorization: Bearer <TOKEN>"
```

---

## 📝 Tech Stack

* ✅ FastAPI
* ✅ Python 3.10+
* ✅ JWT (via PyJWT)
* ✅ SQLite3
* ✅ Swagger UI (auto)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

> Built with ❤️ by [Pruthvi Deepam](https://github.com/yourusername)
