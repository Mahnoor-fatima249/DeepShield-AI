from datetime import datetime, timedelta, timezone
from typing import Any, Union
from jose import jwt # type: ignore
from passlib.context import CryptContext # type: ignore
from app.core.api.v1.config import settings  # type: ignore

# 1. Password Hashing Configuration
# Bcrypt algorithm hashing ke liye sab se secure aur standard mana jata hai
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# 2. Security Functions for Passwords
def verify_password(plain_password: str, hashed_password: str) -> bool:
    """User ke plain password ko hashed password se match karne ke liye"""
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """Registration ke waqt password ko secure hash mein convert karne ke liye"""
    return pwd_context.hash(password)


# 3. JWT Token Generation Infrastructure
def create_access_token(subject: Union[str, Any], expires_delta: timedelta = None) -> str:
    """User Authentication ke liye secure JWT Access Token generate karna"""
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    
    # Token Payload Data Structure
    to_encode = {"exp": expire, "sub": str(subject)}
    
    # Encoding token using Secret Key and Algorithm from config
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt