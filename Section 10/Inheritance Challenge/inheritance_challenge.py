"""
Section 10 Challenge - Inheritance
To help consolidate your understanding of Inheritance, we've got a challenge for you to try out.
The challenge is to create a VampyreKing subclass of Vampyre.

A VampyreKing is going to be incredibly powerful, and any points of damage inflicted will be divided by 4.
VampyreKing objects will also start off with 140 hit points.

So extend Vampyre to create a VampyreKing class with those additional properties.
Test the new class by creating a new VampyreKing object and checking that is does start with 140 hit points
and only takes a quarter of the damage inflicted.
"""
from enemy import VampyreKing

dracula = VampyreKing("Dracula")
print(dracula)
dracula.take_damage(100)
print(dracula)
