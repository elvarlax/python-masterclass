"""
Section 11 Challenge - Store Time Information
The challenge is to store time information in the database so that the original time can be reconstructed.
Whatever else you decide to store, you MUST continue to store the UTC time - that's the only reliable way
to store times so that they are all correct, relative to each other.

Modify the rollback program so that it includes an extra column in the database.
The extra column could be used to store either timezone information,
or the original time's offset from UTC, or the tzinfo. It's up to you what you store.

Modify the code to store the correct information, then modify checkdb to retrieve
the original time and display it along with the UTC time.

Remember to close any open tables and delete the database in the Project pane,
before running your modified program for the first time.

Hints:
1. If you're considering storing a timezone name in the database, stop and reconsider.
You can waste a lof of time finding out that it won't work.
2. You may want to review the videos on pickle in Section 10
(although it's possible to solve this challenge without using pickle).
"""
import sqlite3
import datetime
import pytz
import pickle

db = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)
db.execute("CREATE TABLE IF NOT EXISTS accounts (name TEXT PRIMARY KEY NOT NULL, balance INTEGER NOT NULL)")
db.execute("CREATE TABLE IF NOT EXISTS history (time TIMESTAMP NOT NULL,"
           " account TEXT NOT NULL, amount INTEGER NOT NULL,"
           " zone INTEGER NOT NULL, PRIMARY KEY (time, account))")
db.execute("CREATE VIEW IF NOT EXISTS localhistory AS"
           " SELECT strftime('%Y-%m-%d %H:%M:%f', history.time, 'localtime') AS localtime,"
           " history.account, history.amount FROM history ORDER BY history.time")


class Account(object):

    @staticmethod
    def _current_time():
        utc_time = pytz.utc.localize(datetime.datetime.utcnow())
        local_time = utc_time.astimezone()
        zone = local_time.tzinfo
        return utc_time, zone

    def __init__(self, name: str, opening_balance: int = 0):
        cursor = db.execute("SELECT name, balance FROM accounts WHERE (name = ?)", (name,))
        row = cursor.fetchone()

        if row:
            self.name, self._balance = row
            print("Retrieved record for {}.".format(self.name), end='')
        else:
            self.name = name
            self._balance = opening_balance
            cursor.execute("INSERT INTO accounts VALUES(?, ?)", (name, opening_balance))
            cursor.connection.commit()
            print("Account created for {}.".format(self.name), end='')
        self.show_balance()

    def _save_update(self, amount):
        new_balance = self._balance + amount
        deposit_time, zone = Account._current_time()
        picked_zone = pickle.dumps(zone)
        db.execute("UPDATE accounts SET balance = ? WHERE (name = ?)", (new_balance, self.name))
        db.execute("INSERT INTO history VALUES (?, ?, ?, ?)", (deposit_time, self.name, amount, picked_zone))
        db.commit()
        self._balance = new_balance

    def deposit(self, amount: int) -> float:
        if amount > 0.0:
            self._save_update(amount)
            print("{:.2f} deposited".format(amount / 100))
        return self._balance / 100

    def withdraw(self, amount: int) -> float:
        if 0 < amount <= self._balance:
            self._save_update(-amount)
            print("{:.2f} withdrawn".format(amount / 100))
            return amount / 100
        else:
            print("The amount must be greater than zero and no more than your account balance")
            return 0.0

    def show_balance(self):
        print("Balance on account {} is {:.2f}".format(self.name, self._balance / 100))


if __name__ == '__main__':
    john = Account("John")
    john.deposit(1010)
    john.deposit(10)
    john.deposit(10)
    john.withdraw(30)
    john.withdraw(0)
    john.show_balance()

    terry = Account("TerryJ")
    graham = Account("Graham", 9000)
    eric = Account("Eric", 7000)
    michael = Account("Michael")
    terryG = Account("TerryG")

    db.close()
