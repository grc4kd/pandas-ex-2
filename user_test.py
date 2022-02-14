from db_classes import User
from db_context import AddUser, GetUser

def test_new_user():
    user = User(name="sandy", fullname="Sandy Cheeks")

    assert user.id is None
    assert user.name == "sandy"
    assert user.fullname == "Sandy Cheeks"
    assert user.nickname is None

def test_new_db_user():
    username = "sandy"
    _user = User(name=username, fullname="Sandy Cheeks")

    AddUser(_user)

    user = GetUser(username)

    assert user.id == 1
    assert user.name == "sandy"
    assert user.fullname == "Sandy Cheeks"
    assert user.nickname is None