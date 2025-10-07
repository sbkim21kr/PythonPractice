def validate_username(username):
    if not username:
        raise ValueError("Username cannot be empty")

def validate_password(password):
    if len(password)<6:
        raise ValueError("password must be at least 6 characters long")
    
def validate_email(email):
    if "@" not in email or "." not in email:
        raise ValueError("Email must contain '@' and '.' ")

def validate_input(username, password, email):
    validate_username(username)
    validate_password(password)
    validate_email(email)
    print("All inputs are valid!")

try:
    validate_input("asdffdfd","abc123","sbkim21@gmailcom")
except ValueError as e:
    print("Input error: ",e)


