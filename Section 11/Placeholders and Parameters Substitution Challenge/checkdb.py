"""
Section 11 Challenge - Placeholders and Parameters Substitution
Modify the checkdb program so that it asks the user to enter a name,
then use a WHERE clause in the SQL statement to retrieve just the row for that one person.
"""
import sqlite3

conn = sqlite3.connect("contacts.sqlite")

name = input("Please enter a name: ")

for row in conn.execute("SELECT * FROM contacts WHERE name LIKE ?", (name,)):
    print(row)

conn.close()
