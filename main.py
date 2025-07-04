from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import List
from datetime import datetime, timedelta
import sqlite3
import jwt  # Make sure PyJWT is installed

# --- App Setup ---
app = FastAPI()
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_HOURS = 1

# --- Auth Setup ---
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
fake_user = {"username": "admin", "password": "admin"}

# --- SQLite Setup ---
conn = sqlite3.connect("tasks.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT NOT NULL
    )
""")
conn.commit()

# --- Models ---
class Task(BaseModel):
    title: str
    description: str

class TaskOut(Task):
    id: int

# --- Auth Routes ---
@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.username == fake_user["username"] and form_data.password == fake_user["password"]:
        payload = {
            "sub": form_data.username,
            "exp": datetime.utcnow() + timedelta(hours=ACCESS_TOKEN_EXPIRE_HOURS)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
        if isinstance(token, bytes):
            token = token.decode("utf-8")
        return {"access_token": token, "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid username or password")

# --- Auth Dependency ---
def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload["sub"]
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

# --- Task Routes ---
@app.post("/tasks/", response_model=TaskOut)
def create_task(task: Task, user: str = Depends(get_current_user)):
    cursor.execute("INSERT INTO tasks (title, description) VALUES (?, ?)", (task.title, task.description))
    conn.commit()
    return TaskOut(id=cursor.lastrowid, **task.dict())

@app.get("/tasks/", response_model=List[TaskOut])
def get_tasks(user: str = Depends(get_current_user)):
    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()
    return [TaskOut(id=row[0], title=row[1], description=row[2]) for row in rows]
