from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.api.v1.models.schemas.services.database.session import Base  # type: ignore

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    
    # Account status tracking
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    
    # Timestamp for security audits
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Scan history ke sath relationship line link karne ke liye
    # Is se ek user ke saare scans asani se fetch ho jate hain
    scans = relationship("ScanHistory", back_populates="user", cascade="all, delete-orphan")