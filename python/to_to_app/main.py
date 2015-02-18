from calendar_main import Calendar
from calendar_entry import CalendarEntry
import os
import sqlite3
import datetime

# Creates instances of Calendar and connects to database
cal = Calendar()
db = sqlite3.connect('calendar_db')
cursor = db.cursor()


# Show menu to user until user exits
def display_menu():
    option = 0

    while option != 6:
        print "1. Add entry"
        print "2. Show calendar"
        print "3. Show weekly calendar"
        print "4. Remove entry"
        print "5. Search"
        print "6. Exit"
        option = int(raw_input(">> Select option: "))
        pick_option(option)


# Function to pick a user's menu option
def pick_option(option):
    if option == 1:
        """Add Entry"""
        os.system('clear')
        add_entry()
    elif option == 2:
        """Show Calendar"""
        os.system('clear')
        show_calendar()
    elif option == 3:
        """Show Weekly Calendar"""
        os.system('clear')
        show_week_calendar()
    elif option == 4:
        """Remove Entry"""
        os.system('clear')
        remove_entry()
    elif option == 5:
        """Search Entries"""
        os.system('clear')
        search_entries()
    elif option == 6:
        """Quit Program"""
        os.system('clear')
        db.close()
        print "Thanks for using the To-Do App"


# Adds calendar entry to CalendarEntry class and saves entry to database
def add_entry():
    print "Add Entry:"
    title = raw_input("Title: ")
    description = raw_input("Description: ")
    due_date = raw_input("Due Date: (mm/dd/yyyy): ")

    entry = CalendarEntry(title, description, due_date)
    cal.append_entry(entry)

    # Saves to database
    save_entry_db(title, description, due_date)

    os.system('clear')

    # Does recurrence logic
    recurrence(title, description, due_date)


# Recurrence logic
def recurrence(title, description, due_date):
    recur_entry = raw_input("Add recurrence? ").lower()

    if recur_entry == 'yes' or recur_entry == 'y':
        print "1. Every day (7 days max)"
        print "2. Every week (3 weeks max)"
        option = int(raw_input(">>> Pick option: "))

        if option == 1:
            """Repeat entry every day for 7 days"""
            add_entry_daily(title, description, due_date)
        elif option == 2:
            """Repeat entry every 7 days for 3 weeks"""
            add_entry_weekly(title, description, due_date)

    os.system('clear')
    print "Entry added."


# Add every day recurrence
def add_entry_daily(title, description, due_date):
    # Convert due_date to date format in order to add days to date
    date_in_format = to_date_format(due_date)
    temp_date = date_in_format

    # Create and save recurrence everyday 6 times
    for i in range(6):
        # Add one day to date
        temp_date += datetime.timedelta(days=1)
        # Convert date to string to save to database
        str_date = format_str(temp_date)
        # Add entry to Calendar Entry
        recur_entry = CalendarEntry(title, description, str_date)
        # Add CalendarEntry to Calendar
        cal.append_entry(recur_entry)

        # Saves to database
        save_entry_db(title, description, str_date)


# Add weekly recurrence
def add_entry_weekly(title, description, due_date):
    # Convert due_date to date format in order to add days to date
    date_in_format = to_date_format(due_date)
    temp_date = date_in_format

    # Create and save recurrence everyday 6 times
    for i in range(1, 21, 7):
        # Add 7 days to date
        temp_date += datetime.timedelta(days=7)
        # Convert date to string to save to database
        str_date = format_str(temp_date)
        # Add entry to Calendar Entry
        recur_entry = CalendarEntry(title, description, str_date)
        # Add CalendarEntry to Calendar
        cal.append_entry(recur_entry)

        # Saves to database
        save_entry_db(title, description, str_date)


# Remove entry from calendar
def remove_entry():
    print "Remove Entry:"
    entry = raw_input("Enter entry's title to remove: ")
    cal.remove_entry(entry)

    # Delete from database
    cursor.execute('''DELETE FROM entries WHERE title = ? ''', (entry,))

    db.commit()


# Search entries from calendar
def search_entries():
    entry = raw_input("Enter entry's title to search: ")
    cal.search_entry(entry)


# Convert argument to a different format. Returns string
def format_str(from_var):
    return from_var.strftime('%m/%d/%Y')


# Convert argument to datetime format
def to_date_format(from_var):
    return datetime.datetime.strptime(str(from_var), '%m/%d/%Y')


# Show current week's entries
def show_week_calendar():
    cal.print_week_calendar()


# Gets arguments to store a new entry to database
def save_entry_db(title, description, due_date):
    # Insert entry
    cursor.execute('''INSERT INTO entries(title, description, due_date) VALUES(?,?,?)''', (title, description, due_date))
    db.commit()


# Calls to show full calendar from Calendar class
def show_calendar():
    # PRINTS ALL ENTRIES IN CALENDAR
    cal.print_calendar()


# Reads the database, gets all entries, adds entries to Calendar class
def read_db():
    cursor.execute('''SELECT title, description, due_date FROM entries''')
    all_rows = cursor.fetchall()
    for row in all_rows:
        entry = CalendarEntry(row[0], row[1], row[2])
        cal.append_entry(entry)


# Starts database
def start_db():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS entries(title TEXT, description TEXT, due_date TEXT)
    ''')
    db.commit()


# RUNS PROGRAM
start_db()

read_db()

display_menu()


