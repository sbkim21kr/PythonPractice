# finally is a block that always runs,
# no matter what happens in the try or except.

# It’s used for cleanup tasks — like closing files,
# releasing resources, or printing a final message — even if an error occurred.

file = None
try:
    file=open("output.txt","r")
    content=file.read()
    print(content)
    print("file read successfully")
except FileNotFoundError:
    print("File not found")
finally:
    if file:
        file.close()
        print("file closed")

try:
    print("doing something risky")
    raise ValueError("Oops!")
except ValueError as e:
    print("caught error: ",e)
finally:
    print("goodbye!")