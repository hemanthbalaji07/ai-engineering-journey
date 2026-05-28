# Day 3 - Conditions

# Comparison operators

a = 10
b = 5

print(a == b)   # Equal to
print(a != b)   # Not equal to
print(a > b)    # Greater than
print(a < b)    # Less than
print(a >= b)   # Greater than or equal to
print(a <= b)   # Less than or equal to


# if statement

age = 18

if age >= 18:
    print("You are eligible to vote")


# else statement

age = 15

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")


# elif statement

marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")


# Order matters in conditions

score = 95

if score >= 90:
    print("Excellent")
elif score >= 50:
    print("Pass")
else:
    print("Fail")


# Logical operators

# and -> both conditions must be true

age = 20
has_id = True

if age >= 18 and has_id:
    print("Entry Allowed")


# or -> at least one condition must be true

is_weekend = False
is_holiday = True

if is_weekend or is_holiday:
    print("No School Today")


# not -> reverses boolean value

is_logged_in = False

if not is_logged_in:
    print("Please login")


# Nested conditions

age = 20
has_license = True

if age >= 18:
    if has_license:
        print("You can drive")
    else:
        print("You need a license")
else:
    print("You are underage")


# input with conditions

user_age = int(input("Enter your age: "))

if user_age >= 18:
    print("Adult")
else:
    print("Minor")


# Positive, negative or zero

number = int(input("Enter a number: "))

if number > 0:
    print("Positive Number")
elif number < 0:
    print("Negative Number")
else:
    print("Zero")


# Even or odd

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")


# Divisible by 5

value = int(input("Enter a number: "))

if value % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")


# Multiple conditions together

username = input("Enter username: ")
password = input("Enter password: ")

if username == "hemanth" and password == "python123":
    print("Login Successful")
else:
    print("Invalid Credentials")


# Truthy and falsy values

name = ""

if name:
    print("Name exists")
else:
    print("Name is empty")


cart = [1, 2, 3]

if cart:
    print("Cart has items")
else:
    print("Cart is empty")


# Empty list is falsy

items = []

if items:
    print("List has items")
else:
    print("List is empty")


# Checking boolean conversion

print(bool(0))
print(bool(1))
print(bool(""))
print(bool("Python"))
print(bool([]))
print(bool([1, 2, 3]))


# Ternary operator

age = 20

message = "Adult" if age >= 18 else "Minor"

print(message)