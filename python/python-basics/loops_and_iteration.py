# Loops & Iteration


# for loop

for i in range(5):
    print(i)


# range()

for number in range(3):
    print(number)

for number in range(1, 6):
    print(number)

for number in range(0, 10, 2):
    print(number)


# Iterating through string

language = "Python"

for char in language:
    print(char)


# Iterating through list

fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)


# Using len() with range()

colors = ["red", "blue", "green"]

for index in range(len(colors)):
    print(index, colors[index])


# while loop

count = 1

while count <= 5:
    print(count)
    count += 1


# User input with while loop

password = ""

while password != "python123":
    password = input("Enter password: ")

print("Access Granted")


# break statement

for number in range(1, 11):

    if number == 5:
        break

    print(number)


# continue statement

for number in range(1, 6):

    if number == 3:
        continue

    print(number)


# Nested loops

for i in range(1, 4):

    for j in range(1, 4):
        print(i, j)


# Pattern printing

rows = 5

for i in range(1, rows + 1):
    print("*" * i)


# Reverse loop

for number in range(5, 0, -1):
    print(number)


# enumerate()

languages = ["Python", "Java", "C++"]

for index, language in enumerate(languages):
    print(index, language)


# zip()

names = ["Hemanth", "Rahul", "Arjun"]
scores = [90, 85, 95]

for name, score in zip(names, scores):
    print(name, score)


# Sum of numbers using loop

total = 0

for number in range(1, 6):
    total += number

print(f"Total: {total}")


# Even numbers using loop

for number in range(1, 11):

    if number % 2 == 0:
        print(number)


# Multiplication table

number = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")


# Countdown timer

count = 5

while count > 0:
    print(count)
    count -= 1

print("Time's up")


# Infinite loop with break

while True:

    command = input("Enter quit to stop: ")

    if command == "quit":
        break

print("Loop Ended")