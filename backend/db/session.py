from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.config import settings


SQLALCHEMY_DB_URL = settings.DATABASE_URL
engine = create_engine(SQLALCHEMY_DB_URL)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)