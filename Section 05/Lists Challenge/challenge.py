"""
Section 5 Challenge - Lists
Add to the program below so that if it finds a meal without spam
it prints out each of the ingredients of the meal.
You will need to set up the menu as we did in lines 9-16
"""
menu = []
menu.append(["egg", "spam", "bacon"])
menu.append(["egg", "sausage", "bacon"])
menu.append(["egg", "spam"])
menu.append(["egg", "bacon", "spam"])
menu.append(["egg", "bacon", "sausage", "spam"])
menu.append(["spam", "bacon", "sausage", "spam"])
menu.append(["spam", "egg", "spam", "spam", "bacon", "spam"])
menu.append(["spam", "egg", "sausage", "spam"])

for meal in menu:
    if "spam" not in meal:
        print(meal)
        for ingredient in meal:
            print(ingredient)
