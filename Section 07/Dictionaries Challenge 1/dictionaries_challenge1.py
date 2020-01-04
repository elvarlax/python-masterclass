"""
Section 7 Challenge - Dictionaries 1
Modify the program so that the exits is a dictionary rather than a list,
with the keys being the numbers of the locations and the values being
dictionaries holding the exits (as they do at present). No change should
be needed to the actual code.

Once that is working, create another dictionary that contains words that
players may use. These words will be the keys, and their values will be
a single letter that the program can use to determine which way to go.
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
         5: {"W": 2, "S": 1, "Q": 0}}

directions = {"QUIT": "Q",
              "NORTH": "N",
              "EAST": "E",
              "SOUTH": "S",
              "WEST": "W"}

loc = 1
while True:
    availableExits = ", ".join(exits[loc].keys())

    print(locations[loc])

    if loc == 0:
        break

    direction = input("Available exits are " + availableExits + ": ").upper()
    print()

    if len(direction) > 1:
        words = direction.split()
        for word in words:
            if word in directions:
                direction = directions[word]
                break

    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("You cannot go in that direction")
