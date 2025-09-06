from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.Database.session import get_db
from app.schemas.task import TaskCreate, TaskUpdate,TaskOut
from app.CRUD import task as crud_task
from typing import List

router = APIRouter()

@router.post(
    "/",
    response_model = TaskOut,
    status_code = status.HTTP_201_CREATED,
    summary = "Создать задачу"
)
def create_task(task: TaskCreate, db: Session=Depends(get_db)):
    return crud_task.create_task(db, task)

@router.get(
    "/",
    response_model=List[TaskOut],
)
def read_tasks(skip: int=0, limit: int=10, search: str = None, db:Session=Depends(get_db)):
    return crud_task.get_tasks(db, skip=skip, limit=limit, search= search)

@router.get(
    "/{task_id}",
    response_model = TaskOut,
    summary = "Получить задачу по id"
)
def read_task(task_id: int, db: Session = Depends(get_db)):
    obj = crud_task.get_task(db, task_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    return obj

@router.put(
    "/{task_id}",
    response_model = TaskOut,
    summary = "Обновить задачу"
)
def update_task(task_id: int, task: TaskUpdate, db: Session = Depends(get_db)):
    obj = crud_task.update_task(db, task_id, task)
    if not obj:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    return obj

@router.delete(
    "/{task_id}",
    status_code= status.HTTP_200_OK,
    summary = "Удалить задачу"
)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    ok = crud_task.delete_task(db, task_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    return {"message": f"Задача {task_id}, удалена"}