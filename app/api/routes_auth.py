from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from app.CRUD import user as crud_user
from app.Database.session import get_db
from app.schemas.auth import LoginRequest, TokenResponse
from sqlalchemy.orm import Session

from app.utils.security import verify_password, create_access_token

router = APIRouter()

@router.post("/login", response_model=TokenResponse)

def logining(login: LoginRequest, db: Session=Depends(get_db)):
    user=crud_user.get_user_by_email(db, str(login.email))
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    if not verify_password(login.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="invalid password or email address")
    token = create_access_token({"sub": user.email})
    return TokenResponse(access_token=token, token_type="bearer")