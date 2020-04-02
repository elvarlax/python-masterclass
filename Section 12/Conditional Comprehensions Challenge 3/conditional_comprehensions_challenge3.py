"""
Section 12 Challenge - Conditional Comprehensions 3
For this challenge, convert all comprehensions in the previous challenge to for loops.

We started off by creating a list comprehension from a for loop, this challenge is to go the other way:
convert each of the comprehensions in the previous challenge into a for loop that produces the same result.
"""
locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0},
         }

location = 5

for location in locations:
    forest = []
    for e in exits:
        if location in exits[e].values():
            forest.append((e, locations[e]))
    print("Locations leading to {}:".format(location), end='\t')
    print(forest)
