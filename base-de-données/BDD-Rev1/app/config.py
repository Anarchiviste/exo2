import dotenv
import os
from pathlib import Path


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dotenv.load_dotenv(os.path.join(BASE_DIR, '.env'))


class Config():
    DEBUG = os.getenv("DEBUG", "False").lower() in {"true", "1", "t"}
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")