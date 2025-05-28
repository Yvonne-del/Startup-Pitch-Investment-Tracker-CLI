from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# DB URL

DATABASE_URL = "sqlite:///startup_tracker.db"
engine = create_engine(DATABASE_URL)
# session factory for database operations
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

from .startup import Startup
from .investor import Investor
from .pitch import Pitch


