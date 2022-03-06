import pytest
from db_classes import User, Address
from db_context import DbContext
from sqlalchemy import create_engine

# reusable fixture to run for each test
# create a new engine object for each test / new local db
@pytest.fixture
def new_engine():
    # Create a new Engine instance
    return create_engine("sqlite://", echo=True, future=True)


# one user can have many addresses
def test_new_db_user_with_address(new_engine):
    _context = DbContext(new_engine)
    _user = User(name="sandy", fullname="Sandy Cheeks")
    _address = Address(
        street="16611 Chagrin Blvd",
        city="Shaker Heights",
        state="OH",
        zip="44120"
    )

    _context.AddUser(_user)
    # user must exist before address assignment
    _context.AddUserAddress(_user.name, _address)

    user = _context.GetUser(_user.name)
    address = _context.GetFirstUserAddress(_user.name)

    assert user.id == 1
    assert user.name == "sandy"
    assert user.fullname == "Sandy Cheeks"
    assert user.nickname is None
    assert address.id == 1
    assert address.street == "16611 Chagrin Blvd"
    assert address.city == "Shaker Heights"
    assert address.state == "OH"
    assert address.zip == "44120"


# one user can have many addresses
def test_new_user_with_address(new_engine):
    _context = DbContext(new_engine)
    _user = User(name="sandy", fullname="Sandy Cheeks")
    _address = Address(
        street="16611 Chagrin Blvd",
        city="Shaker Heights",
        state="OH",
        zip="44120"
    )

    # address may exist before user assignment
    _context.AddAddress(_address)
    _context.AddUser(_user)
    _context.AddUserAddress(_user.name, _address)

    address = _context.GetFirstUserAddress(_user.name)

    # address is not duplicated in address table
    assert address.id == 1
    # address has same parts as extant address
    assert address.street == "16611 Chagrin Blvd"
    assert address.city == "Shaker Heights"
    assert address.state == "OH"
    assert address.zip == "44120"
