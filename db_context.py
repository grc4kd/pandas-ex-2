import db_classes
from db_classes import User
from sqlalchemy.orm import sessionmaker

# Create a new Engine instance
from sqlalchemy import create_engine
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)

# Create all tables from class schema
db_classes.Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# add a user
def AddUser(user: User):
    session.add(user)

# get a user
def GetUser(name):
    return session.query(User).filter_by(name=name).first()