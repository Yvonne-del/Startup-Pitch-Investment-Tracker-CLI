# lib/create_db.py
from lib.models import Base, engine

print("Creating all tables...")
Base.metadata.create_all(engine)
print("Done!")
