from calendar import Calendar
from calendar_entry import CalendarEntry

cal = Calendar()


def display_menu():
    option = 0

    while option != 3:
        print "1. Add entry"
        print "2. Show calendar"
        print "3. Exit"
        option = int(raw_input(">> Select option: "))
        pick_option(option)


def pick_option(option):
    if option == 1:
        """Add Entry"""
        add_entry()
    elif option == 2:
        """Show Calendar"""
        show_calendar()
    elif option == 3:
        """Quit Program"""


def add_entry():
    title = raw_input("Title: ")
    description = raw_input("Description: ")
    due_date = raw_input("Due Date: ")

    entry = CalendarEntry(title, description, due_date)
    cal.append_entry(entry)


def show_calendar():

    entry = CalendarEntry("test1", "blah", "02/11/15")
    entrytwo = CalendarEntry("test2", "blah", "02/11/15")
    entrythree = CalendarEntry("test3", "blah", "02/13/15")

    cal.append_entry(entry)
    cal.append_entry(entrytwo)
    cal.append_entry(entrythree)

    # PRINTS ALL ENTRIES IN CALENDAR
    cal.print_calendar()


# RUNS PROGRAM
display_menu()


