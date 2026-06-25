from pydantic import BaseModel
from typing import Optional, Dict, Any
from datetime import datetime

# 1. Base Model: Jo properties har scan schema mein common hain
class ScanBase(BaseModel):
    file_name: str
    file_type: str  # 'image' or 'video'

# 2. Request Schema: Scan create karte waqt jo data chahiye hota hai
class ScanCreate(ScanBase):
    file_hash: str
    prediction: str  # 'REAL' or 'FAKE'
    confidence_score: float
    detailed_analysis: Optional[Dict[str, Any]] = None

# 3. Response Schema: Jab backend frontend ko scan ka result wapas bhejega
class ScanResponse(ScanBase):
    id: int
    user_id: Optional[int] = None
    prediction: str
    confidence_score: float
    detailed_analysis: Optional[Dict[str, Any]] = None
    created_at: datetime

    class Config:
        # Yeh line SQLAlchemy ke database objects ko Pydantic models mein automatically convert karti hai
        from_attributes = True

# 4. History Listing Schema: Sirf dashboard par list dikhane ke liye (chota payload)
class ScanHistoryListItem(BaseModel):
    id: int
    file_name: str
    file_type: str
    prediction: str
    confidence_score: float
    created_at: datetime

    class Config:
        from_attributes = True