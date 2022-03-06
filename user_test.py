import pytest
from db_classes import User
from db_context import DbContext
import sqlalchemy
from sqlalchemy import create_engine


# reusable fixture to run for each test
# create a new engine object for each test / new local db
@pytest.fixture
def new_engine():
    # Create a new Engine instance
    return create_engine("sqlite://", echo=True, future=True)


def test_new_user():
    user = User(name="sandy", fullname="Sandy Cheeks")

    assert user.id is None
    assert user.name == "sandy"
    assert user.fullname == "Sandy Cheeks"
    assert user.nickname is None


def test_new_db_user(new_engine):
    _context = DbContext(new_engine)

    username = "sandy"
    _user = User(name=username, fullname="Sandy Cheeks")

    _context.AddUser(_user)

    user = _context.GetUser(username)

    assert user.id == 1
    assert user.name == "sandy"
    assert user.fullname == "Sandy Cheeks"
    assert user.nickname is None


def test_update_db_user(new_engine):
    _context = DbContext(new_engine)

    username = "pstarfish"
    _user = User(
        name=username,
        fullname="Patrick Star",
        nickname="Patrick"
    )

    _context.AddUser(_user)

    user = _context.GetUser(username)

    user.nickname = "Pat"
    new_username = "patrick"
    user.name = new_username

    user = _context.GetUser(new_username)

    assert user._sa_instance_state.modified is False
    assert user._sa_instance_state.persistent is True
    assert user.id == 1
    assert user.name == "patrick"
    assert user.fullname == "Patrick Star"
    assert user.nickname == "Pat"


def test_attempt_duplicate_username(new_engine):
    _context = DbContext(new_engine)

    username = "pstarfish"
    _user = User(
        name=username,
        fullname="Patrick Star",
        nickname="Patrick"
    )

    _context.AddUser(_user)
    # throw away the user returned from context for testing
    _ = _context.GetUser(username)
    _context = DbContext(new_engine)

    username = "pstarfish"
    _user = User(
        name=username,
        fullname="Phony Baloney",
        nickname="Hatrick"
    )

    with pytest.raises(sqlalchemy.exc.IntegrityError):
        _context.AddUser(_user)

        try:
            _ = _context.GetUser(username)
        except sqlalchemy.exc.IntegrityError as ex:
            print(f"Exception type name: {type(ex).__name__}")
            raise ex
