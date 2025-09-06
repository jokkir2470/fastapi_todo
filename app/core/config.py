import os

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:jS4_CxamOJpO39lHXE@localhost:5432/todo_db"
)