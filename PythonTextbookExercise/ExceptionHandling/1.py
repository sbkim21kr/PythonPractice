class LoginError(Exception):
    def __init__(self, username):
        self.username = username
        super().__init__(f"Login failed for user: {username}")

# Here’s what’s happening:

#     LoginError is a child of Exception

#     super() calls the parent class’s __init__() method

#     That method stores the error message so Python can display it later


# 🧠 Why use super() here?

# Because the parent class (Exception) already knows how to store and display error messages.
# You’re just adding extra info (username) and letting the parent do the rest.

def login(username, password):
    if password != "1234":
        raise LoginError(username)
    print("Login successful!")

try:
    login("sangbum", "1234")
except LoginError as e:
    print("❌ Error caught:", e)

