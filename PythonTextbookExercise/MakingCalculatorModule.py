""" calculator module"""


def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        raise ValueError('cannot divide it by zero')
    return a/b
PI=3.14159
VERSION ="1.0.0"

if __name__ == "__main__":
    print("계산기 모듈이 직접 실행되었습니다.")
    print(f"버전: {VERSION}")
    print(f"add(5, 3) = {add(5, 3)}")
    print(f"subtract(10, 4) = {subtract(10, 4)}")
    print(f"multiply(2, 6) = {multiply(2, 6)}")
    print(f"divide(10, 2) = {divide(10, 2)}")