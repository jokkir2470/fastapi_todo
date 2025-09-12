from passlib.context import CryptContext
from sqlalchemy.util import deprecated
from jose import jwt
from datetime import datetime,timezone, timedelta
from app.core.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES


if not SECRET_KEY:
    raise ValueError("SECRET_KEY is not set in .env file!")


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
def get_password_hash(password: str)->str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str)->bool:
    return pwd_context.verify(plain_password,hashed_password)

def create_access_token(data: dict, expires_delta: timedelta | None = None)->str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encode_jwt