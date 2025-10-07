try:
    with open("data.txt","r") as file:
        content = file.read()
        print("File content:", content)
except FileNotFoundError:
    print("File not found!")

# open("data.txt", "r"): tries to open the file for reading

# If the file doesn’t exist → raises FileNotFoundError

# You catch it and print a friendly message

try:
    with open("output.txt", "w") as file:
        file.write("hello world!!!!!")
        print("file written successfully")
except IOError:
    print("cound not write to file")


file=None
try:
    file=open("output.txt", "r")
    content=file.read()
    print(content)
except FileNotFoundError:
    print("File not found")
finally:
    if file:
        file.close()
        print("file closed")

    