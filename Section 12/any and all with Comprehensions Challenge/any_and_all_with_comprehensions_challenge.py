"""
Section 12 Challenge - any and all with Comprehensions
Use any and a comprehension (or generator expression, if you prefer) to check the plants
in plants_dict to see if there are any grasses in there.

Run your code again, searching for Cactus, to test that it still works when there aren't any.
"""
from data import plants_dict

if any([plant.plant_type == "Grass" for plant in plants_dict.values()]):
    print("This dict contains grasses")
else:
    print("No grasses in this dict")

if any([plant.plant_type == "Cactus" for plant in plants_dict.values()]):
    print("This dict contains cactuses")
else:
    print("No cactuses in this dict")
