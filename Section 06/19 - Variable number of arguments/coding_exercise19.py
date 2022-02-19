"""
Coding Exercise 19 - Variable number of arguments
Write a function to calculate the sum of all numbers passed as its arguments.
Your function should be called sum_numbers and should define a single variable argument
(i.e a star argument) that will get the values to sum.

To pass in this on-line in interpreter, your function must contain a Docstring.

The parameters and return value must be annotated.
Be careful here, you may want to review the lecture Function annotations and type hints,
or check PEP 484 to see what it says about annotating numerical arguments and return types.

Test the function with the following values:
Values              Result
1, 2, 3             6
8, 20, 2            30
12.5, 3.147, 98.1   113.747
1.1, 2.2, 5.5       8.8
"""


def sum_numbers(*values: float) -> float:
    """
    Calculates the sum of all the numbers passed as arguments.

    :param values: The list of numbers as arguments.
    :return: The sum of all the passed arguments.
    """
    return sum(values)


print(sum_numbers(1, 2, 3))
print(sum_numbers(8, 20, 2))
print(sum_numbers(12.5, 3.147, 98.1))
print(sum_numbers(1.1, 2.2, 5.5))
