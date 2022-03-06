import pytest
from db_classes import Address
from db_context import DbContext
from sqlalchemy import create_engine


# reusable fixture to run for each test
# create a new engine object for each test / new local db
@pytest.fixture
def new_engine():
    # Create a new Engine instance
    return create_engine("sqlite://", echo=True, future=True)


def test_new_address():
    address = Address(
        street="16611 Chagrin Blvd",
        city="Shaker Heights",
        state="OH",
        zip="44120"
    )

    assert address.id is None
    assert address.street == "16611 Chagrin Blvd"
    assert address.city == "Shaker Heights"
    assert address.state == "OH"
    assert address.zip == "44120"


def test_new_db_address(new_engine):
    _context = DbContext(new_engine)

    _context.AddAddress(Address(
        street="16611 Chagrin Blvd",
        city="Shaker Heights",
        state="OH",
        zip="44120"
    ))

    addressStr = "16611 Chagrin Blvd, Shaker Heights, OH 44120"
    addressParse = _context.ParseAddress(addressStr)
    address = _context.GetAddress(addressParse)

    assert address.id == 1
    assert address.street == "16611 Chagrin Blvd"
    assert address.city == "Shaker Heights"
    assert address.state == "OH"
    assert address.zip == "44120"
