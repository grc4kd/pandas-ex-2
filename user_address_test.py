from db_classes import User, Address
from db_context import AddUser, AddAddress, AddUserAddress, GetFirstUserAddress, GetUser

# one user can have many addresses
def test_new_user_with_address():
    _user = User(name="sandy", fullname="Sandy Cheeks")
    _address = Address(
        street="16611 Chagrin Blvd",
        city="Shaker Heights",
        state="OH",
        zip="44120"
    )

    AddUser(_user)
    # user must exist before address assignment
    AddUserAddress(_user.name, _address)

    user = GetUser(_user.name)
    address = GetFirstUserAddress(_user.name)

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
def test_new_user_with_address():
    _user = User(name="sandy", fullname="Sandy Cheeks")
    _address = Address(
        street="16611 Chagrin Blvd",
        city="Shaker Heights",
        state="OH",
        zip="44120"
    )

    # address may exist before user assignment
    AddAddress(_address)
    AddUser(_user)
    AddUserAddress(_user.name, _address)

    address = GetFirstUserAddress(_user.name)

    # address is not duplicated in address table
    assert address.id == 1
    # address has same parts as extant address
    assert address.street == "16611 Chagrin Blvd"
    assert address.city == "Shaker Heights"
    assert address.state == "OH"
    assert address.zip == "44120"
