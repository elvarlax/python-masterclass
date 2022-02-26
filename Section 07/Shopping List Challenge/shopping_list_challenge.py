"""
Section 7 Challenge - Shopping List Challenge
At the moment, our program prints out the items that we need to buy.

Just printing to the screen isn't very useful - unless you want to write it down,
or send it to a printer, and take bits of paper when you go shopping.

That's so "last century".

Modify the program, so that it puts the items we need to buy into some sort of data structure.

It's entirely up to you what type of structure you use.

You may decide to create some sort of list, or a dictionary.

The important thing is, that you must produce something that can be iterated over,
to retrieve the ingredient and quantity.

Hint: We did something similar with the buy_computer_dict program, earlier in this section.

Another hint: Whatever data structure you choose, use a function to add the items to it.
"""
from contents import pantry, recipes


def add_shopping_item(data: dict, item: str, amount: int) -> None:
    """Add `item` and `amount` to the `data` dict."""
    data[item] = data.setdefault(item, 0) + amount


display_dict = {}
for index, key in enumerate(recipes):
    display_dict[str(index + 1)] = key

shopping_list = {}
while True:
    # Display the menu of recipes we know how to cook
    print("Please choose your recipe")
    print("-------------------------")
    for key, value in display_dict.items():
        print(f"{key} - {value}")

    choice = input(": ")

    if choice == "0":
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f"You have selected {selected_item}")
        print("checking ingredients ...")
        ingredients = recipes[selected_item]
        print(ingredients)
        for food_item, required_quantity in ingredients.items():
            quantity_in_pantry = pantry.get(food_item, 0)
            if required_quantity <= quantity_in_pantry:
                print(f"\t{food_item} OK")
            else:
                quantity_to_buy = required_quantity - quantity_in_pantry
                print(f"\tYou need to buy {quantity_to_buy} of {food_item}")
                add_shopping_item(shopping_list, food_item, quantity_to_buy)

print("\nShopping list:")
for items in shopping_list.items():
    print(items)
