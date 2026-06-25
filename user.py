from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import datetime
from app.schemas.scan import ScanHistoryListItem  # type: ignore

# 1. Base User Schema: Jo properties registration aur profile dono mein share hoti hain
class UserBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=50, description="Username kam se kam 3 characters ka hona chahiye")
    email: EmailStr

# 2. Registration Schema: Jab naya user account banaye ga
class UserCreate(UserBase):
    password: str = Field(..., min_length=6, description="Password kam se kam 6 characters ka hona chahiye")

# 3. Response Schema: Jab backend frontend ko user ka data wapas bhejega (Isme password nahi hota!)
class UserResponse(UserBase):
    id: int
    is_active: bool
    is_superuser: bool
    created_at: datetime

    class Config:
        from_attributes = True

# 4. Detailed Profile Schema: User ke data ke sath uski scan history bhi fetch karne ke liye
class UserProfileWithHistory(UserResponse):
    scans: List[ScanHistoryListItem] = []

    class Config:
        from_attributes = True

# 5. Token Schemas: Login ke baad JWT token return karne ke liye
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None