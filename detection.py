from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
import uuid

# Database aur AI Engine ke correct absolute paths
from app.core.api.v1.models.schemas.services.database.session import get_db # type: ignore
from app.core.api.v1.models.schemas.services.ai_detector import DeepfakeDetector # type: ignore

# Schemas aur Models ke correct absolute paths (Dots completely khatam)
from app.core.api.v1.models.schemas.scan import ScanResponse # type: ignore
from app.core.api.v1.models.scan import ScanHistory # type: ignore

router = APIRouter(prefix="/detection", tags=["Deepfake Detection Engine"])