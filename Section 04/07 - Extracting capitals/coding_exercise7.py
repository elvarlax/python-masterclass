"""
Coding Exercise 7 - Extracting capitals
Write a program to print out the capital letters in the string

"Alright, but apart from the Sanitation, the Medicine, Education,
Wine, Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?"
"""
quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""
for i in quote:
    if i.istitle():
        print(i)
