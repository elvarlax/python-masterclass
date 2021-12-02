"""
Coding Exercise 14 - The Magical Adder
For this exercise, you have to write a python program which prompts the user to enter three
integers separated by ",".

The user input is of the form: a, b, c where a, b and c are numbers.

Your program should calculate and display the result of the calculation:
a + b - c

Examples:
    1. Please enter three numbers 10,11,10
    11

    2. Please enter three numbers 7,5,-1
    13
"""
a, b, c = input("Please enter three numbers: ").split(",")
result = int(a) + int(b) - int(c)
print(result)
