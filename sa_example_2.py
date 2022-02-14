from db_classes import User
from db_context import AddUser, GetUser

# Create new user
sandy = User(name="sandy", fullname="Sandy Cheeks")
print(sandy)

# Add our user to the session
AddUser(sandy)

# Get data from pending instance
our_user = GetUser("sandy")
print(our_user)
