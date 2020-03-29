"""
Section 11 Challenge - Star Args
Write a function called build_tuple that takes a variable number of arguments,
and returns a tuple containing the values passed to it.

Example of input to the function, and the expected output:

message_tuple = build_tuple("hello", "planet", "earth", "take", "me", "to", "your", "leader")
print(type(message_tuple))
print(message_tuple)

number_tuple = build_tuple(1, 2, 3, 4, 5, 6)
print(type(number_tuple))
print(number_tuple)

<class 'tuple'>
('hello', 'planet', 'earth', 'take', 'me', 'to', 'your', 'leader')
<class 'tuple'>
(1, 2, 3, 4, 5, 6)
"""


def build_tuple(*args):
    return args


message_tuple = build_tuple("hello", "planet", "earth", "take", "me", "to", "your", "leader")
print(type(message_tuple))
print(message_tuple)

number_tuple = build_tuple(1, 2, 3, 4, 5, 6)
print(type(number_tuple))
print(number_tuple)
