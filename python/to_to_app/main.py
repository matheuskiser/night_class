from calendar_main import Calendar
from calendar_entry import CalendarEntry
import os
import sqlite3

# Creates instances of Calendar and connects to database
cal = Calendar()
db = sqlite3.connect('calendar_db')
cursor = db.cursor()


# Show menu to user until user exits
def display_menu():
    option = 0

    while option != 4:
        print "1. Add entry"
        print "2. Show calendar"
        print "3. Show weekly calendar"
        print "4. Exit"
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
    print "Entry added."


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


