# Day 2 - Arithmetic Operators and Strings

a = 10
b = 5

print("Value of a:", a)
print("Value of b:", b)


# Addition
print("Addition:", a + b)

# Subtraction
print("Subtraction:", a - b)

# Multiplication
print("Multiplication:", a * b)

# Division always returns float
print("Division:", a / b)

# Floor division removes decimal part
print("Floor Division:", a // b)

# Modulus gives remainder
print("Modulus:", a % b)

# Exponent
print("Exponent:", a ** b)


# More examples

x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)
print(x % y)
print(x ** y)


# Checking datatype
print(type(x / y))


# User input with arithmetic operators

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Floor Division:", num1 // num2)
print("Modulus:", num1 % num2)
print("Exponent:", num1 ** num2)


# f-strings

name = "Hemanth"
age = 18
course = "Python"

print(f"My name is {name}")
print(f"I am {age} years old")
print(f"I am learning {course}")

print(f"Sum of 10 and 5 is {10 + 5}")


# String methods

text = "   Python Programming Language   "

print(text)


# upper()
print(text.upper())

# lower()
print(text.lower())

# strip()
print(text.strip())

# replace()
print(text.replace("Python", "Java"))

# split()
print(text.split())


# Strings are immutable

language = "python"

print(language)

language.upper()

# Original string does not change
print(language)

# Reassigning updated value
language = language.upper()

print(language)


# More string examples

message = "  Hello World  "

print(message.upper())
print(message.lower())
print(message.strip())
print(message.replace("World", "Python"))
print(message.split())