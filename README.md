# FastAPI Todo API

Простое REST API для управления задачами, созданное с использованием FastAPI и SQLAlchemy.

## 🚀 Технологии

- **FastAPI** - современный веб-фреймворк для создания API
- **SQLAlchemy** - ORM для работы с базой данных
- **SQLite** - легковесная база данных
- **Pydantic** - валидация данных
- **Uvicorn** - ASGI сервер

## 📋 Возможности

- ✅ Создание задач (CREATE)
- ✅ Получение списка задач (READ)
- ✅ Обновление задач (UPDATE)
- ✅ Удаление задач (DELETE)
- ✅ Автоматическая документация API (Swagger UI)
- ✅ Валидация данных с помощью Pydantic

## 🛠️ Установка и запуск

### 1. Клонируйте репозиторий

```bash
git clone https://github.com/TrueCookie/fastapi-todo.git
cd fastapi-todo
```

### 2. Создайте виртуальное окружение

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate
```

### 3. Установите зависимости

```bash
pip install -r requirements.txt
```

### 4. Запустите сервер

```bash
uvicorn app.main:app --reload
```

Сервер будет доступен по адресу: `http://127.0.0.1:8000`

## 📖 Документация API

После запуска сервера документация доступна по адресам:

- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

## 🔗 API Endpoints

| Метод | Endpoint | Описание |
|-------|----------|----------|
| GET | `/` | Корневой endpoint |
| GET | `/todos` | Получить все задачи |
| GET | `/todos/{id}` | Получить задачу по ID |
| POST | `/todos` | Создать новую задачу |
| PUT | `/todos/{id}` | Обновить задачу |
| DELETE | `/todos/{id}` | Удалить задачу |

## 📝 Примеры использования

### Создание задачи

```bash
curl -X POST "http://127.0.0.1:8000/todos" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Изучить FastAPI",
    "description": "Пройти документацию",
    "completed": false
  }'
```

### Получение всех задач

```bash
curl -X GET "http://127.0.0.1:8000/todos"
```

### Обновление задачи

```bash
curl -X PUT "http://127.0.0.1:8000/todos/1" \
  -H "Content-Type: application/json" \
  -d '{
    "completed": true
  }'
```

## 📂 Структура проекта

```
fastapi-todo/
├── app/
│   ├── __init__.py
│   ├── main.py          # Точка входа, роуты
│   ├── models.py        # SQLAlchemy модели
│   ├── schemas.py       # Pydantic схемы
│   └── database.py      # Подключение к БД
├── venv/
├── requirements.txt
├── todos.db            # SQLite база данных (создаётся автоматически)
└── README.md
```

## 🤝 Вклад в проект

Буду рад любым предложениям и улучшениям! Создавайте Issues и Pull Requests.

## 📄 Лицензия

MIT License
