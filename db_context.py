import db_classes
from db_classes import User, Address
from sqlalchemy.orm import sessionmaker


# Create a new Engine instance
from sqlalchemy import create_engine, select
engine = create_engine("sqlite://", echo=True, future=True)

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
    stmt = (
        select(User).
        where(User.name == name)
    )
    result = session.execute(stmt)
    for row in result.scalars():
        return row


# add an address
def AddAddress(address: Address):
    # do not add duplicate addresses
    if (GetAddress(address) is None):
        session.add(address)


# add an address for to a user
# one user may have many addresses
def AddUserAddress(name, address: Address):
    _user = GetUser(name)
    
    # check to see if this address exists in the db already
    _address = GetAddress(address)
    if (_address is None):
        # add missing address to db
        AddAddress(address)
        _address = GetAddress(address)
    
    # link user to address
    _user.addresses.append(_address)


# get an address, by scanning for address attrs
def GetAddress(address: Address):
    stmt = (
        select(Address).
        where(
            Address.street==address.street,
            Address.city==address.city,
            Address.state==address.state,
            Address.zip==address.zip
        ).limit(1)
    )
    result = session.execute(stmt)
    for row in result.scalars():
        return row


# get an address, by parsing an address string
def ParseAddress(addressStr):
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

    _address = Address(
        street=_street,
        city=_city,
        state=_state,
        zip=_zip
    )
    return GetAddress(_address)


# get the first address for a user
# based on their user name
def GetFirstUserAddress(name):
    _user = GetUser(name)
    stmt = (
        select (Address).
        where (Address.user_id==_user.id)
    )
    result = session.execute(stmt)
    for row in result.scalars():
        return row
