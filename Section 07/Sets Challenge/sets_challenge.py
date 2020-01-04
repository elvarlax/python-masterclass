"""
Section 7 Challenge - Sets
Create a program that takes some text and returns a list of
all the characters in the text that are not vowels,
sorted in alphabetical order.

You can either enter the text from the keyboard or
initialise a string variable with the string.
"""
text = "Python is a very powerful language"
vowels = {"a", "e", "i", "o", "u"}
result = sorted(set(text).difference(vowels))
print(result)
