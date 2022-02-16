"""
Section 6 Challenge - Palindrome Function
Fix our is_palindrome function so that it ignores the case of the letters,
when checking if the two strings are equal.

Remember to test the function with words that are palindromes, using a mix of upper and lower case letters.
Also test that it correctly identifies words that aren't palindromes.
"""


def is_palindrome(string):
    return string[::-1].casefold() == string.casefold()


word = input("Please enter a word to check: ")
if is_palindrome(word):
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")
