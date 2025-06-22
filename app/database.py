from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

# Construct the SQLAlchemy connection string
DATABASE_URL = f"postgresql+psycopg2://{settings.db_user}:{settings.db_password}@{settings.db_host}:{settings.db_port}/{settings.db_name}?sslmode=require"

# Engine
engine = create_engine(DATABASE_URL)

# Sesion
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define Base class that are gona be from what the models will expand
Base = declarative_base()


# dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
