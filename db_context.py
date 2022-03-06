import db_classes
from db_classes import User, Address
from sqlalchemy import select
import sqlalchemy.orm
from sqlalchemy.orm import sessionmaker


class DbContext():
    session: sqlalchemy.orm.Session = None

    def __init__(self, engine):
        # Create all tables from class schema
        db_classes.Base.metadata.create_all(engine)

        # Create a session
        Session = sessionmaker(bind=engine)
        self.session = Session()

    # add a user
    def AddUser(self, user: User):
        self.session.add(user)

    # get a user
    def GetUser(self, name):
        stmt = (
            select(User).
            where(User.name == name)
        )
        result = self.session.execute(stmt)
        return result.scalars().first()

    # add an address
    def AddAddress(self, address: Address):
        # do not add duplicate addresses
        if (self.GetAddress(address) is None):
            self.session.add(address)

    # add an address for to a user
    # one user may have many addresses
    def AddUserAddress(self, name, address: Address):
        _user = self.GetUser(name)

        # check to see if this address exists in the db already
        _address = self.GetAddress(address)
        if (_address is None):
            # add missing address to db
            self.AddAddress(address)
            _address = self.GetAddress(address)

        # link user to address
        _user.addresses.append(_address)

    # get an address, by scanning for address attrs
    def GetAddress(self, address: Address):
        stmt = (
            select(Address).
            where(
                Address.street == address.street,
                Address.city == address.city,
                Address.state == address.state,
                Address.zip == address.zip
            ).limit(1)
        )
        result = self.session.execute(stmt)
        for row in result.scalars():
            return row

    # get an address, by parsing an address string
    def ParseAddress(self, addressStr):
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
        return _address

    # get the first address for a user
    # based on their user name
    def GetFirstUserAddress(self, name):
        _user = self.GetUser(name)
        stmt = (
            select(Address).
            where(Address.user_id == _user.id)
        )
        result = self.session.execute(stmt)
        for row in result.scalars():
            return row
