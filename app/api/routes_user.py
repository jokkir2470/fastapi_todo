from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.Database.session import get_db
from app.schemas.user import UserCreate, UserOut
from app.CRUD import user as crud_user
from typing import List

router = APIRouter()

@router.post(
    "/",
    response_model=UserOut,
    status_code=status.HTTP_201_CREATED,
    summary="Создать пользователя"
)

def user_create(user: UserCreate, db:Session = Depends(get_db)):
    db_user = crud_user.get_user_by_email(db, str(user.email))
    if db_user:
        raise HTTPException(status_code=400, detail="Email уже зарегестрирован")
    return crud_user.user_create(db, user)

@router.get(
    "/{user_id}",
    response_model=UserOut,
    summary="Найти пользователя по id"
)
def get_user_by_id(user_id: int, db:Session=Depends(get_db)):
    obj = crud_user.get_user_by_id(db, user_id)
    if not obj:
        raise HTTPException(status_code=404, detail="User not found")
    return obj

@router.get(
    "/",
    response_model=List[UserOut],
    summary="Список пользователей с пагинацией"
)
def read_users(skip: int=0, limit: int=10, db:Session=Depends(get_db)):
    return crud_user.get_user(db, skip = skip, limit = limit)