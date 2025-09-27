PI=3.14159

def circle_area(radius):
    return PI*radius**2
def circle_circumference(radius):
    return 2*PI*radius
def rectangle_area(width,height):
    return width*height
class Calculator:
    def add(self, a, b):
        return a+b
    def subtract(self,a,b):
        return a-b
    def multipy(self,a,b):
        return a*b
    def divide(self,a,b):
        if b!=0:
            return a/b
        else:
            return "cannot divide by zero"
if __name__ =="__main__":
    print("the model math_utils has been executed.")
    print(f"PI: {PI}")

# Every Python file has a built-in variable called __name__.

# When you run a Python file directly, __name__ is set to "__main__".

# When the same file is imported as a module in another file, __name__ is set to the module’s filename (e.g., "math_utils").

# Purpose: This if block ensures that the code inside it runs only when you execute the file directly, not when it’s imported.

