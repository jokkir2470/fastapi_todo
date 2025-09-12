from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from app.utils.security import get_password_hash

def user_create(db: Session, user_in: UserCreate)->User:
    hashed_pw = get_password_hash(user_in.password)
    obj = User(
        username= user_in.username,
        email=str(user_in.email),
        hashed_password=hashed_pw
    )
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_user_by_email(db:Session, email: str)->User | None:
    return db.query(User).filter(User.email==email).first()

def get_user(db: Session,skip: int=0, limit:int=10):
    return db.query(User).offset(skip).limit(limit).all()

def get_user_by_id(db:Session, user_id: int)-> User | None:
    return db.query(User).filter(User.id==user_id).first()

