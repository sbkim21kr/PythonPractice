from utils import add, subtract

def main():
    """Main logic of the program"""
    print("This is a simple calculator.")
    
    num1 = 10
    num2 = 5
    
    result_add = add(num1, num2)
    print(f"{num1} + {num2} = {result_add}")
    
    result_subtract = subtract(num1, num2)
    print(f"{num1} - {num2} = {result_subtract}")

if __name__ == "__main__":
    main()