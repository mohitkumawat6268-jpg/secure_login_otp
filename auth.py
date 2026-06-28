import bcrypt
from database import add_user, get_user


def register(username, password):
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    add_user(username, hashed)
    print("✅ User registered successfully")


def login(username, password):
    user = get_user(username)

    if not user:
        print("❌ User not found")
        return False

    stored_password = user[2]

    if bcrypt.checkpw(password.encode(), stored_password):
        return True
    else:
        print("❌ Wrong password")
        return False