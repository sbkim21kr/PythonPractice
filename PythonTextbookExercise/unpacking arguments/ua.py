# unpacking arbitrary positional arguments
def sum_three_numbers(a,b,c):
    print(f"Sum:{a+b+c}")

numbers = [3443,344,334]
sum_three_numbers(*numbers)




# unpacking arbitrary keyword arguments
def display_person_info(name, age, city):
    print(f"Name: {name}, Age: {age}, City: {city}")

person_data={"name":"KSB","age":43, "city":"Incheon"}
display_person_info(**person_data)