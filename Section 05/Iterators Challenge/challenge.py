"""
Section 5 Challenge - Iterators
Create a list of items (you may use either strings or numbers in the list),
then create an iterator using the iter() function.

Use a for loop to loop "n" times, where n is the number of items in your list.
Each time round the loop, use next() on your list to print the next item.

hint: use the len() function rather than counting the number of items in the list.
"""
my_list = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
my_iterator = iter(my_list)
for i in range(len(my_list)):
    print(next(my_iterator))
