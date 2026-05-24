# Day 1 - Variables
# A variable is a container for storing data values.

name = "Hemanth Balaji"  # String
age = 18  # Integer
cgpa = 8.5  # Float
is_student = True  # Boolean

# Printing the Output
print("Name:", name)
print("Age:", age)
print("CGPA:", cgpa)
print("Is Student:", is_student)

# type() shows the datatype of a variable
print(type(name))
print(type(age))
print(type(cgpa))
print(type(is_student))

# Variables can be reassigned with new values
city = 'chennai'
print("City:", city)
# Updating variable with new value
city = 'bangalore'
print("Updated City:", city)

# Python is dynamically typed language. 
# The same variable can hold different datatypes at different times.
data = 67
print(data)
print(type(data))

data = "Python Programming"
print(data)
print(type(data))

# Multiple variables can be assigned in one line.
x, y, z = "Hemanth", 18, "Python"
print(x)
print(y)
print(z)
# One value can also be assigned to multiple variables.
a = b = c = "Hello"
print(a)
print(b)
print(c)

# Variable names
# Variable names must start with a letter or an underscore.
my_name = "Hemanth"

# Variable names cannot start with a number or contain spaces.

# 1name = "Hemanth"  # Invalid variable name
# my name = "Hemanth"  # Invalid variable name


# Python variable names are case-sensitive
# The variable 'name' and 'Name' are different variables. 

name = "Hemanth"
Name = "Balaji"

print(name)
print(Name)