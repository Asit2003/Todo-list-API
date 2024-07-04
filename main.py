from fastapi import FastAPI, HTTPException, Query, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from models import TodoItem
from typing import List
import secrets

app = FastAPI()
security = HTTPBasic()

# In-memory "database"
db: List[TodoItem] = []

# Simple function to verify username and password
def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, "admin")
    correct_password = secrets.compare_digest(credentials.password, "secret")
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

@app.post("/todos/", response_model=TodoItem)
def create_todo_item(todo: TodoItem, username: str = Depends(get_current_username)):
    todo.id = len(db) + 1
    db.append(todo)
    return todo

@app.get("/todos/", response_model=List[TodoItem])
def read_all_todo_items(page: int = 1, size: int = 10, username: str = Depends(get_current_username)):
    start = (page - 1) * size
    end = start + size
    return db[start:end]

@app.get("/todos/{todo_id}", response_model=TodoItem)
def read_todo_item(todo_id: int, username: str = Depends(get_current_username)):
    for todo in db:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo item not found")

@app.put("/todos/{todo_id}", response_model=TodoItem)
def update_todo_item(todo_id: int, updated_todo: TodoItem, username: str = Depends(get_current_username)):
    for index, todo in enumerate(db):
        if todo.id == todo_id:
            updated_todo.id = todo_id
            db[index] = updated_todo
            return updated_todo
    raise HTTPException(status_code=404, detail="Todo item not found")

@app.delete("/todos/{todo_id}", response_model=dict)
def delete_todo_item(todo_id: int, username: str = Depends(get_current_username)):
    for index, todo in enumerate(db):
        if todo.id == todo_id:
            del db[index]
            return {"message": "Todo item deleted"}
    raise HTTPException(status_code=404, detail="Todo item not found")
