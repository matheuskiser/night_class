import operator
import datetime
import os
from utils import Utils


class Calendar(Utils):

    def __init__(self):
        self.calendar_dictionary = []
        self.today = None
        self.start_week = None
        self.end_week = None
        self.get_today_date()
        self.get_week_bound()

    # Adds entry to Calendar list
    def append_entry(self, entry):
        self.calendar_dictionary.append(entry)

    # Sorts calendar by ascending order by date
    def sort_calendar(self):
        cal = sorted(self.calendar_dictionary, key=operator.attrgetter('entry_due_date'))
        return cal

    # Sets self.today to today's date
    def get_today_date(self):
        # Get today's date
        date = datetime.datetime.now().date()
        # Convert date
        now_date_string = self.format_str(date)
        # Convert now_date to datetime
        today_date = self.to_date_format(now_date_string)
        # Sets result to today attribute
        self.today = today_date

    # Sets self.start_week and .end_week
    def get_week_bound(self):
        # Calculate start and end of current week
        start_week = self.today - datetime.timedelta(self.today.weekday()+1)
        end_week = start_week + datetime.timedelta(6)

        # Convert start and end week dates
        st_week = self.format_str(start_week.date())
        ed_week = self.format_str(end_week.date())

        # Convert start and end week dates to datetime
        first_week = self.to_date_format(st_week)
        last_week = self.to_date_format(ed_week)

        # Set attributes to first and last week variables
        self.start_week = first_week
        self.end_week = last_week

    # Prints entire calendar
    def print_calendar(self):

        # Sort calendar_dictionary by due_date in ascending order
        sorted_dictionary = self.sort_calendar()

        # Outputs to user all entries formatted
        print "All entries:"
        temp_date = None
        for i in sorted_dictionary:
            # Convert entry_date to datetime format
            entry_date = self.to_date_format(i.get_due_date())
            # If current entry's date is today or later
            if entry_date >= self.today:
                # If current entry's due_date does not equal to previous entry, then output the date
                if temp_date != i.get_due_date():
                    print "\nDATE: " + str(i.get_due_date()) + "\n"
                    print i
                else:
                    print i

                temp_date = i.get_due_date()

    # Returns weekly calendar
    def print_week_calendar(self):

        # Sorts calendar dictionary to be ascending by date
        sorted_dictionary = self.sort_calendar()

        print "Current week's entries"
        temp_date = None
        for i in sorted_dictionary:
            # Convert entry_date to datetime format
            entry_date = self.to_date_format(i.get_due_date())
            # If current entry's date is within current week, then print
            if self.start_week <= entry_date <= self.end_week:
                # If current entry's due_date does not equal to previous entry, then output the date
                if temp_date != i.get_due_date():
                    print "\nDATE: " + str(i.get_due_date()) + "\n"
                    print i
                else:
                    print i

                temp_date = i.get_due_date()

    # Creates a list comprehension with only items that are not the ones to be removed
    def remove_values_from_list(self, the_list, val):
        return [value for value in the_list if value.get_title() != val]

    # Remove entry from calendar list
    def remove_entry(self, entry_title):

        # Records length of list before remove
        len_orig = len(self.calendar_dictionary)

        # Removes all entry_title from calendar list, then resets calendar
        x = self.remove_values_from_list(self.calendar_dictionary, entry_title)
        self.calendar_dictionary = x

        # Check if length of previous list is less than list after remove
        if len_orig > len(self.calendar_dictionary):
            os.system('clear')
            print "'" + entry_title + "' entry has been deleted."
        else:
            print "No entry found."

    # Search entries in calendar dictionary
    def search_entry(self, entry_title):
        # If result comes up with something, then true
        found = False

        # Sorts calendar dictionary to be ascending by date
        sorted_dictionary = self.sort_calendar()

        print "Search results"
        temp_date = None
        for i in sorted_dictionary:
            if i.get_title().lower() == entry_title.lower():
                found = True
                # If current entry's due_date does not equal to previous entry, then output the date
                if temp_date != i.get_due_date():
                    print "\nDATE: " + str(i.get_due_date()) + "\n"
                    print i
                else:
                    print i

                temp_date = i.get_due_date()

        if not found:
            print "No entries found."
