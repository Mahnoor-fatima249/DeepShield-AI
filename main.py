from fastapi import FastAPI
from app.core.api.v1.models.schemas.services.database.session import engine, Base  # type: ignore
from app.core.api.v1 import detection  # type: ignore

# CRITICAL FIX: Dono models ko yahan import karna zaroori hai 
# taake metadata ko tables ki relationship samajh aa sake
from app.core.api.v1.models.user import User  # type: ignore
from app.core.api.v1.models.scan import ScanHistory  # type: ignore

# Database tables auto-create karne ke liye (Ab dono tables mil jayenge)
Base.metadata.create_all(bind=engine)

# FastAPI Initialize
app = FastAPI(
    title="Deepfake Detection Platform",
    description="Advanced AI + Cyber Security Infrastructure for Deepfake Analysis",
    version="1.0.0"
)

# Routes ko register karein
app.include_router(detection.router)

@app.get("/")
async def root():
    return {
        "status": "online",
        "message": "Deepfake Detection Secure Backend is running successfully. Core Engine Active."
    }