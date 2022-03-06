from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    fullname = Column(String)
    nickname = Column(String)

    addresses = relationship("Address", back_populates="user")

    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r},\
            fullname={self.fullname!r})"


class Address(Base):
    __tablename__ = 'address'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    street = Column(String)
    city = Column(String)
    state = Column(String)
    zip = Column(String)

    user = relationship("User", back_populates="addresses")

    def __repr__(self):
        return f"Address(id={self.id!r}, {self.street}, {self.city},\
            {self.state} {self.zip})"
