"""
Section 6 Challenge - Binary
When converting a decimal number to binary, you look for the highest power
of 2 smaller than the number and put a 1 in that column. You then take the
remainder and repeat the process with the next highest power - putting a 1
if it goes into the remainder and a zero otherwise. Keep repeating until you
have dealt with all powers down to 2 ** 0 (i.e., 1).

Write a program that requests a number from the keyboard, then prints out
its binary representation.

Obviously you could use a format string, but that is not allowed for this
challenge.

The program should cater for numbers up to 65535; i.e. (2 ** 16) - 1

Hint: you will need integer division (//), and modulo (%) to get the remainder.
You will also need ** to raise one number to the power of another:
For example, 2 ** 8 raises 2 to the power 8.

As an optional extra, avoid printing leading zeros.
"""
powers = []
for power in range(15, -1, -1):
    powers.append(2 ** power)
print(powers)

x = int(input("Please enter a number: "))
printing = False
for power in powers:
    bit = x // power
    if bit != 0 or power == 1:
        printing = True
    if printing:
        print(bit, end='')
    x %= power
