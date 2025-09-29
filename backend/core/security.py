from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt
from core.config import SECRET_KEY, ALGORITHM

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# creating hashed password
def hash_password(password: str):
    return pwd_context.hash(password)

# verifying the password
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# creating jwt tokens
def create_access_token(data: dict, expires_delta: int = 30):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=expires_delta)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)