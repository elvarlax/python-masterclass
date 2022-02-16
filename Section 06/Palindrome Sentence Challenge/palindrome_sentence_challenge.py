"""
Section 6 Challenge - Palindrome Sentence
Create a new function called palindrome_sentence.

The function should return True if the sentence is a palindrome - False, otherwise.

Remember that we ignore spaces, punctuations and things like tabs and line feeds.
We're only interested in alphanumeric characters.

Check out the Strings Methods in the documentation, to find one that's suitable for
identifying if a character is alphanumeric.

There are two methods you could use, depending on whether you want to allow numbers or not.

Once you've excluded invalid characters from the string, the remainder of the function will
be very similar to what we did for the is palindrome function.

Some examples of palindrome sentences are:
- Was it a car, or a cat, I saw?
- Do geese see god?
- Desnes not far, Raf ton sensed

Googling will find more examples.
Remember to also test with sentences that aren't palindromes.
"""


def is_palindrome(string):
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    return is_palindrome(string)


word = input("Please enter a word to check: ")
if is_palindrome(word):
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")