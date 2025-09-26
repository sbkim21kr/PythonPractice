# arbitrary positional arguments, arbitrary keyword arguments



# In Python, a tuple is an immutable, ordered collection of elements. That means:

# ✅ Ordered: The elements have a defined sequence and can be accessed by index.

# 🔒 Immutable: Once created, the contents of a tuple cannot be changed (no adding, removing, or modifying elements).

# 📦 Heterogeneous: Tuples can contain elements of different types (e.g., integers, strings, lists).



# *args: 위치 매개변수를 튜플로 받음
def sum_all(*numbers):
    """모든 숫자를 더하는 함수"""
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_all(1, 2, 3))           # 6
print(sum_all(1, 2, 3, 4, 5))     # 15
print(sum_all(10))                # 10
print(sum_all())                  # 0

# **kwargs: 키워드 매개변수를 딕셔너리로 받음
def print_info(**info):
    """정보를 출력하는 함수"""
    print("=== 정보 출력 ===")
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="김철수", age=25, city="서울",height="178cm")
print_info(product="노트북", price=1200000, brand="삼성")

# *args와 **kwargs를 함께 사용
def flexible_function(required_param, *args, **kwargs):
    """유연한 매개변수를 받는 함수"""
    print(f"필수 매개변수: {required_param}")
    print(f"추가 위치 매개변수: {args}")
    print(f"키워드 매개변수: {kwargs}")

flexible_function("essential item", 1, 2, 3, "toronto",5,6,7,name="홍길동", age=30, city="seoul", literacy="high")
#  📌 Parameter Order Rules in Python

#     When defining a function, parameters must follow this order:

#     Positional-only parameters (rare, using /)

#     Regular positional parameters (like required_param)

#            *args — captures additional positional arguments

#     Keyword-only parameters (after *, optional)

#            **kwargs — captures additional keyword arguments