"""
Section 8 Challenge - CSV DictReader Challenge
Modify the code in countries.py that reads the data to create the countries dictionary.
Your new code should use a DictReader to read country_info.txt as CSV file.

The new dictionary should be the same structure as the current one.
The keys will be the country names, and the values will be dictionaries that the DictReader produces.

WARNING: The column heading in country_info.txt are in proper case - they start with an uppercase letter.
The abbreviations are all in capitals.

You will need to change the "capital" key that's used in the while loop, to reflect that difference.

That should be the only change that you make inside the while loop.

If you've been experimenting with your countries.py file,
you can download my code from countries.txt in the resources,
and paste it into a new file for this challenge.

I'll be calling my solution file dict_reader_challenge.py
"""
import csv

input_filename = 'country_info.txt'

countries = {}
with open(input_filename, encoding='utf-8', newline='') as country_file:
    reader = csv.DictReader(country_file, delimiter='|')
    for row in reader:
        countries[row['Country'].casefold()] = row
        countries[row['CC'].casefold()] = row

while True:
    chosen_country = input('Please enter the name of a country: ')
    country_key = chosen_country.casefold()
    if country_key in countries:
        country_data = countries[country_key]
        print(f"The capital of {chosen_country} is {country_data['Capital']}")
    elif chosen_country == 'quit':
        break
