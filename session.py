from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Local SQLite Database file ka naam aur path
# Yeh automatically aapke project directory mein 'deepfake_platform.db' naam ki file bana dega
DATABASE_URL = "sqlite:///./deepfake_platform.db"

# 1. Database Engine Create Karein
# 'check_same_thread: False' sirf SQLite ke liye zaroori hai taake FastAPI ke multiple requests handle ho sakein
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

# 2. Session Maker (Database Transactions handle karne ke liye)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 3. Base Class (Isi class ko extend karke hamare models tables bante hain)
Base = declarative_base()

# 4. Dependency Injection Function
# Yeh function FastAPI ke endpoints (routes) mein database connection handle karega
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()