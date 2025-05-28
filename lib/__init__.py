from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine("sqlite:///yourdb.db")  # or your chosen DB URI
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

# Import your models here to register them with Base
from lib.models.startup import Startup
from lib.models.pitch import Pitch
from lib.models.investor import Investor
