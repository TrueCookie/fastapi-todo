from pydantic import BaseModel
from typing import Optional

# Схема для создания задачи
class TodoCreate(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

# Схема для обновления задачи
class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

# Схема для ответа
class TodoResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    completed: bool

    class Config:
        from_attributes = True