from sqlalchemy.orm import Session
from app.models.todo import Task
from app.schemas.task import TaskCreate, TaskUpdate

def create_task(db: Session, task_in: TaskCreate)->Task:
    obj = Task(**task_in.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_tasks(db:Session, skip: int = 0, limit: int= 10, search: str= None):
    query = db.query(Task)
    if search:
        query = query.filter(Task.title.ilike(f"%{search}%"))
    return query.offset(skip).limit(limit).all()

def get_task(db: Session, task_id: int)->Task | None:
    return db.query(Task).filter(Task.id==task_id).first()

# def list_task(db: Session, skip: int=0, limit: int = 100) ->list[type[Task]]:
#     return db.query(Task).offset(skip).limit(limit).all()

def update_task(db: Session, task_id: int,task_in: TaskUpdate)-> Task | None:
    obj = get_task(db,task_id)
    if not obj:
        return None
    data = task_in.model_dump()
    obj.title = data["title"]
    obj.description = data["description"]
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def delete_task(db: Session, task_id: int)->bool:
    obj = get_task(db, task_id)
    if not obj:
        return False
    db.delete(obj)
    db.commit()
    return True
