# Day 1 - Variables and Data Types

# String
name = "Hemanth Balaji"

# Integer
age = 18

# Float
cgpa = 8.5

# Boolean
is_student = True


# Printing values
print("Name:", name)
print("Age:", age)
print("CGPA:", cgpa)
print("Is Student:", is_student)


# Checking datatypes
print(type(name))
print(type(age))
print(type(cgpa))
print(type(is_student))


# Variables can be changed
city = "Chennai"

print("City:", city)

city = "Bangalore"

print("Updated City:", city)


# Python is dynamically typed
data = 67

print(data)
print(type(data))

data = "Python Programming"

print(data)
print(type(data))


# Multiple variables in one line
x, y, z = "Hemanth", 18, "Python"

print(x)
print(y)
print(z)


# Same value to multiple variables
a = b = c = "Hello"

print(a)
print(b)
print(c)


# Variable naming rules

my_name = "Hemanth"

# Invalid variable names

# 1name = "Hemanth"
# my name = "Hemanth"


# Variables are case-sensitive
name = "Hemanth"
Name = "Balaji"

print(name)
print(Name)


# input()

user_name = input("Enter your name: ")

print("Hello,", user_name)

print(type(user_name))


# input() always returns string

user_age = int(input("Enter your age: "))

print("Your age is:", user_age)

print(type(user_age))


# float input

user_cgpa = float(input("Enter your CGPA: "))

print("Your CGPA is:", user_cgpa)

print(type(user_cgpa))


# Without int()

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

print(num1 + num2)


# With int()

num1 = int(input("Enter first number again: "))
num2 = int(input("Enter second number again: "))

print(num1 + num2)