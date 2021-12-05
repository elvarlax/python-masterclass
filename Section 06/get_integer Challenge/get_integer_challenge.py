"""
Section 6 Challenge - get_integer
Modify the get_integer function so that it prints a message,
if the user enters an invalid numbers.
"""
import random


def get_integer(prompt):
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)


highest = 1000
answer = random.randint(1, highest)
print(answer)
guess = 0
print(f"Please guess number between 1 and {highest}")

while guess != answer:
    guess = get_integer(": ")

    if guess == 0:
        break
    if guess == answer:
        print("Well done, you guessed it")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:
            print("Please guess lower")
