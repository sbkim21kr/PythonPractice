class EmptyUsernameError(Exception):
    def __init__(self):
        super().__init__("Username cannot be empty")

class PasswordTooShortError(Exception):
    def __init__(self, length):
        super().__init__(f"password is too short. minimum length is {length} characters")

def login(username, password):
    if not username:
        raise EmptyUsernameError()
    if len(password)<6:
        raise PasswordTooShortError(6)
    print("Login successful!")

try:
    login("","abc")
except EmptyUsernameError as e:
    print("Error:", e)
except PasswordTooShortError as e:
    print("Error:", e)

