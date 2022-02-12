from db_classes import User, Address

# Create a new Engine instance
from sqlalchemy import create_engine
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)

# Setting up the ORM Registry
from sqlalchemy.orm import registry
mapper_registry = registry()

sandy = User(name="sandy", fullname="Sandy Cheeks")

print(sandy)