"""
Section 11 Challenge - Exceptions
Create a new Python file, and write a short program to ask the user to type in two integer numbers,
then print out their first number divided by their second.
The program shouldn't crash, no matter what the user types in (although you don't have to worry about Ctrl keys).
Hint: If you have to do the same thing more than once, that sounds like a good use for a function.
"""
import sys


def get_number(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("Invalid number")
        except EOFError:
            sys.exit(0)


first_number = get_number("Please enter the first number: ")
second_number = get_number("Please enter the second number: ")

try:
    print("{} divided by {} is {}".format(first_number, second_number, first_number / second_number))
except ZeroDivisionError:
    print("Cannot divide by zero")
