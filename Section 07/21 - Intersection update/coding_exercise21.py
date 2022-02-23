"""
Coding Exercise 21 - Intersection update
Your task for this coding exercise is to find out which prepositions have been used in the quote:

"Education is not the learning of facts but the training of the mind to think – Albert Einstein"

There are two steps you'll need to perform:

1. Split text to create a list of words.
2. Create an intersection of the set of words with the prepositions set that we've provided in the exercise code.

In order for the on-line checker to validate your solution, it's essential that you use the name
preps_used for the interaction that you create.
"""
text = """Education is not the learning of facts
but the training of the mind to think

– Albert Einstein"""

prepositions = {"as", "but", "by", "down", "for", "in", "of", "on", "to", "with"}

preps_used = prepositions.intersection(text.split())
print(preps_used)
