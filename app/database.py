import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

if os.getenv("DB_type") == "supabase":
    # Fetch variables
    DB_USER = os.getenv("SB_USER")
    DB_PASSWORD = os.getenv("SB_PASSWORD")
    DB_HOST = os.getenv("SB_HOST")
    DB_PORT = os.getenv("SB_PORT")
    DB_NAME = os.getenv("SB_NAME")

    # Construct the SQLAlchemy connection string
    DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?sslmode=require"
else:
    # DB configuration
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_NAME = os.getenv("DB_NAME")
    DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

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
