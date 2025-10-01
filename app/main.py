from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from . import models, schemas
from .database import engine, get_db

# Создаём таблицы в БД
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Todo API",
    description="API для управления задачами",
    version="1.0.0"
)

# GET все задачи
@app.get("/todos", response_model=List[schemas.TodoResponse])
def get_todos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    todos = db.query(models.Todo).offset(skip).limit(limit).all()
    return todos

# GET одна задача
@app.get("/todos/{todo_id}", response_model=schemas.TodoResponse)
def get_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo не найдена")
    return todo

# POST создать задачу
@app.post("/todos", response_model=schemas.TodoResponse, status_code=201)
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    db_todo = models.Todo(**todo.model_dump())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

# PUT обновить задачу
@app.put("/todos/{todo_id}", response_model=schemas.TodoResponse)
def update_todo(todo_id: int, todo: schemas.TodoUpdate, db: Session = Depends(get_db)):
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo не найдена")
    
    update_data = todo.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_todo, key, value)
    
    db.commit()
    db.refresh(db_todo)
    return db_todo

# DELETE удалить задачу
@app.delete("/todos/{todo_id}", status_code=204)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo не найдена")
    
    db.delete(db_todo)
    db.commit()
    return None

# Корневой endpoint
@app.get("/")
def root():
    return {"message": "Todo API работает! Документация: /docs"}