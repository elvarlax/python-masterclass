"""
Section 9 Challenge - Timezone
Create a program that allows a user to choose one of
up to 9 time zones from a menu. You can choose any
zones you want from the all_timezones list.

The program will then display the time in that timezone, as
well as local time and UTC time.

Entering 0 as the choice will quit the program.

Display the dates and times in a format suitable for the
user of your program to understand, and include the
timezone name when displaying the chosen time.
"""
import datetime
import pytz

timezones = {'1': "Iceland",
             '2': "Europe/Copenhagen",
             '3': "Europe/Stockholm",
             '4': "Europe/London",
             '5': "Europe/Madrid",
             '6': "Europe/Paris",
             '7': "Europe/Rome",
             '8': "Europe/Berlin",
             '9': "Europe/Amsterdam"}

print("Please choose a time zone (or 0 to quit): ")
for timezone in sorted(timezones):
    print("\t{}. {}".format(timezone, timezones[timezone]))

while True:
    choice = input()
    if choice == 0:
        break
    if choice in timezones.keys():
        tz_to_display = pytz.timezone(timezones[choice])
        world_time = datetime.datetime.now(tz=tz_to_display)
        print("The time in {} is {} {}".format(timezones[choice], world_time.strftime('%A %x %X %z'),
                                               world_time.tzname()))
        print("Local time is {}".format(datetime.datetime.now().strftime('%A %x %X')))
        print("UTC is {}".format(datetime.datetime.utcnow().strftime('%A %x %X')))
    else:
        print("Please choose a time zone (or 0 to quit): ")
