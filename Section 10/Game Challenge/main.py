"""
Section 10 Challenge - Game Challenge
Modify the Player class so that the players' scores are increased by one thousand
every time their level increases by one.
So if they jump up two levels, they'll get a bonus of two thousand added to their score.

If the player drops back a level, they'll lose one thousand for each level they drop back.
They can't go below Level One, so your solution should prevent that from happening.

The aim of this challenge is to practice properties, so although it may make more sense to add methods
to increase and decrease the level, please don't do it that way - use a property.
"""
from player import Player

elvar = Player("Elvar")

print(elvar.name)
print(elvar.lives)
elvar.lives -= 1
print(elvar)

elvar.lives -= 1
print(elvar)

elvar.lives -= 1
print(elvar)

elvar.lives -= 1
print(elvar)

elvar._lives = 9
print(elvar)

elvar.level = 2
print(elvar)

elvar.level += 5
print(elvar)

elvar.level = 3
print(elvar)
