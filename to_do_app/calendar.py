import operator
import datetime


class Calendar(object):

    calendar_list = []
    previous_date = ""

    def __init__(self):
        date = datetime.datetime.now()
        self.day = date.day
        self.month = date.month
        self.year = date.year

    def add_to_calendar(self, entry):
        self.calendar_list.append(entry)

    def display_calendar(self):

        sorted_list = self.sort_list()

        # display list
        for i in sorted_list:
            print i

    def sort_list(self):
        # Sorts list of entries by date
        sorted_list = sorted(self.calendar_list, key=operator.attrgetter('date'))
        return sorted_list
