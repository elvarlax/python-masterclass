"""
Section 11 Challenge - Generators
Create a generator to return an infinite sequence of odd numbers, starting at 1.

Print the first 100 numbers, to check that the generator's working correctly.

Note that this is just for testing. We're going to need far more than 100 numbers,
and don't know in advance how many, so that's why we're creating our own generator,
instead of just using range.
"""


def odd_numbers():
    number = 1
    while True:
        if number % 2 != 0:
            yield number
        number += 1


odd_numbers = odd_numbers()

for i in range(100):
    print(next(odd_numbers))
