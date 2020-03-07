"""
Section 10 Challenge - Vampyre Challenge
Create a new Vampyre class that's a subclass of Enemy.

Vampyres have 3 lives, and take 12 hitpoints of damage.

You can create a new Python file for the Vampyre if you like,
but I'd suggest adding it to the existing enemy.py file.

Test your class by creating one or two Vampyre instances and displaying their details.
Also inflict some damage to make sure the take_damage methods works ok.

Also make sure that the trolls can also take damage, because we haven't tested that yet.
"""
from enemy import Troll, Vampyre

ugly_troll = Troll("Pug")
print("Ugly troll - {}".format(ugly_troll))

another_troll = Troll("Ug")
print("Another troll - {}".format(another_troll))
another_troll.take_damage(18)
print(another_troll)

brother = Troll("Urg")
print(brother)

ugly_troll.grunt()
another_troll.grunt()
brother.grunt()

dracula = Vampyre("Dracula")
amber = Vampyre("Amber")

print(dracula)
dracula.take_damage(10)
print(dracula)

print(amber)
amber.take_damage(7)
print(amber)
