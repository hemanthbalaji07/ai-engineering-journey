# Functions & Scope


# Function definition

def greet():
    print("Hello, Python")


greet()


# Function with parameters

def greet_user(name):
    print(f"Hello, {name}")


greet_user("Hemanth")
greet_user("Rahul")


# Function with multiple parameters

def student_info(name, age):
    print(f"Name: {name}")
    print(f"Age: {age}")


student_info("Hemanth", 18)


# Return statement

def add(a, b):
    return a + b


result = add(10, 5)

print(result)


# Returning multiple values

def calculate(a, b):

    addition = a + b
    subtraction = a - b

    return addition, subtraction


sum_result, sub_result = calculate(20, 10)

print(sum_result)
print(sub_result)


# Default arguments

def greet_user(name="Guest"):
    print(f"Hello, {name}")


greet_user()
greet_user("Hemanth")


# Keyword arguments

def employee(name, role):
    print(f"{name} works as a {role}")


employee(role="Developer", name="Hemanth")


# *args

def add_numbers(*numbers):

    total = 0

    for number in numbers:
        total += number

    return total


print(add_numbers(10, 20))
print(add_numbers(10, 20, 30, 40))


# **kwargs

def display_profile(**details):

    for key, value in details.items():
        print(f"{key}: {value}")


display_profile(
    name="Hemanth",
    age=18,
    city="Chennai"
)


# Local scope

def show_number():

    number = 100

    print(number)


show_number()

# print(number)
# This will cause an error because
# number exists only inside the function.


# Global scope

course = "Python"


def show_course():
    print(course)


show_course()
print(course)


# Local and global variables

value = 50


def test():

    value = 100

    print(f"Inside Function: {value}")


test()

print(f"Outside Function: {value}")


# Using global keyword

count = 0


def increase_count():

    global count

    count += 1


increase_count()
increase_count()

print(count)


# User input with functions

def square(number):
    return number * number


user_number = int(input("Enter a number: "))

print(square(user_number))


# Even or odd using function

def check_even_odd(number):

    if number % 2 == 0:
        return "Even"

    return "Odd"


num = int(input("Enter a number: "))

print(check_even_odd(num))


# Function inside loop

def multiplication_table(number):

    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")


table_number = int(input("Enter a number: "))

multiplication_table(table_number)


# Refactoring repeated code into function

def line():
    print("-" * 30)


line()
print("Student Details")
line()

print("Marks")
line()


# Lambda function

square = lambda x: x * x

print(square(5))