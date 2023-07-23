import os
from dataclasses import dataclass
from dotenv import load_dotenv
from pathlib import Path

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

ENV_PATH = Path(ROOT_DIR) / ".env"
load_dotenv(dotenv_path=ENV_PATH)


@dataclass
class Settings:
    PROJECT_NAME: str = "Pars Bloggers"
    VERSION: str = "1.0.0"

    DEBUG = (os.getenv("DEBUG", "False") == "True")

    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER = os.getenv("POSTGRES_SERVER", "127.0.0.1")
    POSTGRES_PORT = os.getenv("POSTGRES_PORT", 5432)
    POSTGRES_DB = os.getenv("POSTGRES_DB")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

    SECRET_KEY = os.getenv("SECRET_KEY")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30



settings = Settings()