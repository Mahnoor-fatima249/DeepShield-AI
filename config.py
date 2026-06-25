import os
from pydantic_settings import BaseSettings    # type: ignore

class Settings(BaseSettings):
    # 1. System Metadata
    PROJECT_NAME: str = "Deepfake Detection Platform"
    API_V1_STR: str = "/api/v1"
    
    # 2. Security & Cyber Security Infrastructure
    # Note: Real environment mein yeh keys .env file se load hongi
    SECRET_KEY: str = os.getenv("SECRET_KEY", "SUPER_SECRET_CYBER_SECURITY_KEY_DO_NOT_SHARE_12345")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 24 Hours tokens valid rahega
    
    # 3. Database Connection
    # By default, local SQLite database use hoga ('deepfake_platform.db')
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./deepfake_platform.db")
    
    # 4. Cyber Security & AI Engine Upload Restrictions
    ALLOWED_IMAGE_EXTENSIONS: list = ["jpg", "jpeg", "png", "webp"]
    ALLOWED_VIDEO_EXTENSIONS: list = ["mp4", "avi", "mov", "mkv"]
    MAX_UPLOAD_SIZE_MB: int = 50  # 50MB tak ki video processing support
    
    # 5. AI Engine Threshold
    # Agar model ka confidence score isse upar hoga toh hi 'FAKE' trigger hoga
    DEEPFAKE_DETECTION_THRESHOLD: float = 0.75 

    class Config:
        case_sensitive = True

# Global object jise baqi files mein use kiya ja sake
settings = Settings()