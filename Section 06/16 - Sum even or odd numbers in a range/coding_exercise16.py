"""
Coding Exercise 16 - Sum even or odd numbers in a range
In this coding exercise, you have to write a function named sum_eo with the following parameters:

n: a positive number
t: a str

If t has the value 'e', the function should return the sum of all even natural numbers less than n.
Else if t has the value 'o', the function should return the sum of all odd natural numbers less than n.
For any other values of t return -1.

Examples:
    1. sum_eo(10, 'e') should return 20, since 2 + 4 + 6 + 8 = 20
    2. sum_eo(7, 'o') should return 9, since 1 + 3 + 5 = 9
    3. sum_eo(11, 'spam') should return -1.
"""


def sum_eo(n, t):
    """
    Sum even or odd numbers in range.
    Return the sum of even or odd natural numbers, in the range 1..n-1.

    :param n: The endpoint of the range. The numbers from 1 to n-1 will be summed.
    :param t: 'e' to sum even numbers, 'o' to sum odd numbers.
    :return: The sum of the even or odd numbers in the range.
             Returns -1 if `t` is not 'e' or 'o'.
    """
    if t == "e":
        start = 2
    elif t == 'o':
        start = 1
    else:
        return -1

    return sum(range(start, n, 2))


print(sum_eo(10, 'e'))
print(sum_eo(7, 'o'))
print(sum_eo(11, 'spam'))
