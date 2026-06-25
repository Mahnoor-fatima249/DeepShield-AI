from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.api.v1.models.schemas.services.database.session import Base  # type: ignore

class SystemHistoryLog(Base):
    __tablename__ = "system_history_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True) # Kis user ne action kiya
    action_type = Column(String, nullable=False) # 'SCAN_IMAGE', 'LOGIN', 'DELETE_HISTORY'
    status = Column(String, nullable=False) # 'SUCCESS', 'FAILED'
    ip_address = Column(String, nullable=True) # Security audit ke liye user ka IP
    browser_agent = Column(String, nullable=True) # Device details
    meta_data = Column(JSON, nullable=True) # Extra info track karne ke liye
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # User ke sath simple link setup
    user = relationship("User")