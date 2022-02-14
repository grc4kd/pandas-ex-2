import db_classes
from db_classes import User
from sqlalchemy.orm import sessionmaker

# Create a new Engine instance
from sqlalchemy import create_engine
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)

# Create all tables from class schema
db_classes.Base.metadata.create_all(engine)

# Create new user
sandy = User(name="sandy", fullname="Sandy Cheeks")
print(sandy)

# Create a session

Session = sessionmaker(bind=engine)
session = Session()

# Add our user to the session
session.add(sandy)

# Get data from pending instance
our_user = session.query(User).filter_by(name='sandy').first()

print(our_user)
