# FastAPI Todo List API

This project is a simple Todo List API built with FastAPI that allows users to perform CRUD operations on todo items.

## Features


- Create, read, update, and delete todo items.
- Basic HTTP authentication to protect the endpoints.
- Pagination for listing todo items.
- In-memory storage for simplicity and demonstration purposes.

## Requirements

- Python
- FastAPI
- Uvicorn
- Pydantic
- fastapi-security

## Installation

Clone this repository:
```bash
git clone https://github.com/Asit2003/Todo-list-API.git
cd Todo-list-API
```
Setup a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```
Install the dependencies:

```bash
pip install -r requirements.txt
```
## Running the Application
Start the server:
```bash
uvicorn main:app --reload
```

## API Endpoints


- This will start the server on http://127.0.0.1:8000. 
- The --reload flag enables auto-reloading so the server will restart after code changes.
- You can visit http://127.0.0.1:8000/docs to access the API documentation and test the endpoints interactively.

## Authentication
All endpoints require basic HTTP authentication. Use the following credentials for access:

- Username: `admin`
- Password: `secret`

## CRUD Operations

- ``POST /todos/``: Create a new todo item

- ``GET /todos/``: List all todo items

- `GET /todos/{todo_id}`: Get a single todo item by ID

- `PUT /todos/{todo_id}`: Update a todo item

- `DELETE /todos/{todo_id}`: Delete a todo item
