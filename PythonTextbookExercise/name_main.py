def say_hello(name):
    return f"hello, {name}!!!"

# “Run this block only if this file is being executed directly — not imported as a module.”
if __name__ == "__main__":
    user_name="Rick"
    greeting=say_hello(user_name)
    print(greeting)
# Every Python file has a special built-in variable called __name__

# If the file is run directly → __name__ == "__main__"

# If the file is imported → __name__ == "filename"