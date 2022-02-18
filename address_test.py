from db_classes import Address
from db_context import AddAddress, ParseAddress


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


def test_new_db_address():
    addressStr = "16611 Chagrin Blvd, Shaker Heights, OH 44120"
    _address = Address(
        street="16611 Chagrin Blvd",
        city="Shaker Heights",
        state="OH",
        zip="44120"
    )

    AddAddress(_address)

    address = ParseAddress(addressStr)

    assert address.id == 1
    assert address.street == "16611 Chagrin Blvd"
    assert address.city == "Shaker Heights"
    assert address.state == "OH"
    assert address.zip == "44120"
