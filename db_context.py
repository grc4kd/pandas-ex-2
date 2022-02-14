import db_classes
from db_classes import User, Address
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


# add an adress
def AddAddress(address: Address):
    session.add(address)


# get an address, by parsing an address string
def GetAddress(addressStr):
    addressParts = addressStr.split(",")

    # read-in address in order, street number and name first
    if (len(addressParts[0]) > 0):
        _street = addressParts[0].lstrip().rstrip()

    # then the city
    if (len(addressParts[1]) > 0):
        _city = addressParts[1].lstrip().rstrip()

    # and finally the state and zip code
    if (len(addressParts[2]) > 0):
        _statezip = addressParts[2].lstrip().rstrip()

    # split the state and zip strings
    addressParts = _statezip.split(" ")
    if (len(addressParts[0]) > 0):
        _state = addressParts[0]

    if (len(addressParts[1]) > 0):
        _zip = addressParts[1]

    return session.query(Address).filter_by(
            street=_street,
            city=_city,
            state=_state,
            zip=_zip
        ).first()
