"""
Section 11 Challenge - SQL in Python
Create a new Python file, and write the code to print
out all the records in the contacts.sqlite database

Check the result, and explain why it's not what we'd expect.
"""
import sqlite3

db = sqlite3.connect("contacts.sqlite")

for name, phone, email in db.execute("SELECT * FROM contacts"):
    print(name)
    print(phone)
    print(email)
    print("-" * 20)

db.close()

# contacts2.py file needs to have update_cursor.connection.commit() in order to update the contacts.
# To solve this challenge is to add update_cursor.connection.commit() on line 11 in the contacts2.py file.
