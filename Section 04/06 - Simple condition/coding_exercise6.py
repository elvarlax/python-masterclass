"""
Coding Exercise 6 - Simple condition
Write a small program that assigns the value 5 to one variable,
called x, and the value 7 to another, called y.

Your program should then use an if statement to compare the values,
and print out 'x is greater than y' if x is greater,
or 'x is smaller than y' if y is greater.
If x equals y, print out 'x equals y'
"""
x = 5
y = 7

if x > y:
    print("x is greater than y")
elif x < y:
    print("x is smaller than y")
else:
    print("x equals y")
