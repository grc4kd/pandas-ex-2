from db_classes import User, Address
from db_context import AddAddress, GetAddress, AddUser, GetUser

# Create new user
sandy = User(name="sandy", fullname="Sandy Cheeks")
print(sandy)

# Add our user to the session
AddUser(sandy)

# Get data from pending instance
our_user = GetUser("sandy")
print(our_user)

# add/get address
address = Address(
        street="16611 Chagrin Blvd",
        city="Shaker Heights",
        state="OH",
        zip="44120"
    )

AddAddress(address)
our_address = GetAddress("16611 Chagrin Blvd, Shaker Heights, OH 44120")
print(our_address)
