import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DEBUG = os.getenv("DEBUG", True)
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", 8000))
    WORKERS = int(os.getenv("WORKERS", 4))
    
    # Database
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")
    
    # Model settings
    MODEL_PATH = os.getenv("MODEL_PATH", "./models")
    MAX_MODEL_SIZE = 5 * 1024 * 1024 * 1024  # 5GB
    
    # API settings
    API_TITLE = "AI Platform"
    API_VERSION = "1.0.0"
    API_DESCRIPTION = "High-performance AI model serving platform"
