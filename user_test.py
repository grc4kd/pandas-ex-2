from db_classes import User

def test_new_user():
    user = User(name="sandy", fullname="Sandy Cheeks")

    assert user.id == None
    assert user.name == "sandy"
    assert user.fullname == "Sandy Cheeks"
    assert user.nickname == None