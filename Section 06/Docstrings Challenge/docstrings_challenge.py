"""
Section 6 Challenge - Docstrings
Create Docstrings for the three functions that we wrote, in the functions.py module.

Check your Docstrings by using Ctrl-Q (Ctrl-J on a Mac), to make sure they're formatted correctly,
and provide all the information someone would need, to use the functions.

Note: make sure you test your functions, after adding the Docstrings, to make sure you haven't broken anything.
"""


def multiply(x, y):
    """
    Multiply 2 numbers.

    This function is intended to multiply two numbers,
    but you can also use it to multiply a sequence.
    For example, if you pass a string as the first argument,
    the return value will be the string repeated `y` times.

    :param x: The first number to multiply.
    :param y: The number to multiply `x` by.
    :return: The product of `x` and `y`.
    """
    result = x * y
    return result


def is_palindrome(string):
    """
    Check if a string is a palindrome.

    A palindrome is a word that can be read both backwards and forwards.

    :param string: The string to check.
    :return: True if `string` is a palindrome, False otherwise.
    """
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(sentence):
    """
    Check if a sentence is a palindrome.

    This function ignores sentence spaces, capital letters, and punctuation.

    :param sentence: The sentence to check.
    :return: True if `sentence` is a palindrome, False otherwise.
    """
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    return is_palindrome(string)
