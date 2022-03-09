"""
Section 7 Challenge - Simple Deep Copy Challenge
Write a function that takes a dictionary as an argument, and returns a deep copy of the dictionary.

You're going to write your own function, to do a similar job to the deepcopy function that we've just used.
But you'll do it without using the copy module.

Your function will be a lot simpler than deepcopy. It only has to cope with 1 level of contained objects.
It should be able to successfully copy dictionaries like our animals or recipes dictionaries.

It doesn't have to handle dictionaries that contain objects that also contain objects.
That's much too difficult at this stage.

The basic approach will be to create a new, empty dictionary.

Next, iterate over the keys and values of the dictionary that's being copied.

For each key, copy the value, then add the copy of the value to the new dictionary.

Your function only has to handle values that are dictionaries or lists.
Both of those objects have a copy method.
"""
from contents import recipes


def my_deepcopy(d: dict) -> dict:
    """Copy a dictionary, creating copies of the `list` or `dict` values.

    The function will crash with an AttributeError if the values aren't lists or dictionaries.

    :param d: The dictionary to copy.
    :return: A copy of `d`, with the values being copies of the original values.
    """
    copy_dict = {}
    for key, value in d.items():
        if isinstance(value, list):
            value_list = value.copy()
            copy_dict[key] = value_list
            return copy_dict
        elif isinstance(value, dict):
            value_dict = value.copy()
            copy_dict[key] = value_dict
            return copy_dict
        else:
            raise AttributeError("Values aren't lists or dictionaries!")


recipes_copy = my_deepcopy(recipes)
recipes_copy["Butter chicken"]["ginger"] = 300
print(recipes_copy["Butter chicken"]["ginger"])
print(recipes["Butter chicken"]["ginger"])
