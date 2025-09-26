print("-------------------------------------")

fruits=["apple","kiwi","banana"]
# fruits is a ITERABLE data
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
print("-------------------------------------")
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")

print("-------------------------------------")

names=["Anthony","Lebron","Dwyane"]
ages=[25,30,35]
cities=["Denver","Cleveland","Miami"]
print("-------------------------------------")
print(f"{'Name':<10}{'Age':<5}{'City':<10}")
print("-"*30)

for name,age,city in zip(names,ages,cities):
    print(f"{name:<10}{age:<5}{city:<10}")

print("-------------------------------------")
person_dict=dict(zip(names, ages))
print(person_dict)

print("-------------------------------------")
print(list(range(5)))
print(list(range(2,8)))
print(list(range(0,10,2)))
print(list(range(10,0,-1)))
print("-------------------------------------")
print(list(reversed([1,2,3,4])))
print(list(reversed("Python")))
print("-------------------------------------")
numbers=[5,7,3,46,67]
print(sorted(numbers))
print(sorted(numbers,reverse=True))
print("-------------------------------------")
words = ["python","java","c++","javascript"]
print(sorted(words))
print(sorted(words, key=len, reverse=False))
print("-------------------------------------")
scores = [85, 92, 78, 96, 88]
print(f"all scores are above 60: {all(score >= 60 for score in scores)}")
print(f"is there any score above 90: {any(score >= 90 for score in scores)}")