import operator
import datetime


class Calendar(object):

    def __init__(self):
        self.calendar_dictionary = []

    def append_entry(self, entry):
        self.calendar_dictionary.append(entry)

    def sort_calendar(self):
        cal = sorted(self.calendar_dictionary, key=operator.attrgetter('entry_due_date'))
        return cal

    def print_calendar(self):

        # Sort calendar_dictionary by due_date in ascending order
        sorted_dictionary = self.sort_calendar()

        # Outputs to user all entries formatted
        print "All entries:"
        temp_date = None
        for i in sorted_dictionary:
            # If current entry's due_date does not equal to previous entry, then output the date
            if temp_date != i.get_due_date():
                print "\nDATE: " + str(i.get_due_date()) + "\n"
                print i
            else:
                print i

            temp_date = i.get_due_date()

    def print_week_calendar(self):
        sorted_dictionary = self.sort_calendar()

        # Get today's date
        date = datetime.datetime.now().date()
        # Convert date
        now_date = datetime.datetime.strptime(str(date), "%Y-%m-%d").strftime('%m/%d/%Y')
        # Convert now_date to datetime
        curr_entry_date = datetime.datetime.strptime(str(now_date), '%m/%d/%Y')

        # Calculate start and end of current week
        start_week = curr_entry_date - datetime.timedelta(curr_entry_date.weekday()+1)
        end_week = start_week + datetime.timedelta(6)

        # Convert start and end week dates
        st_week = datetime.datetime.strptime(str(start_week.date()), "%Y-%m-%d").date().strftime('%m/%d/%Y')
        ed_week = datetime.datetime.strptime(str(end_week.date()), "%Y-%m-%d").date().strftime('%m/%d/%Y')

        # Convert start and end week dates to datetime
        first_week = datetime.datetime.strptime(str(st_week), '%m/%d/%Y')
        last_week = datetime.datetime.strptime(str(ed_week), '%m/%d/%Y')

        print "Current week's entries"
        temp_date = None

        for i in sorted_dictionary:
            # Convert entry_date to datetime format
            entry_date = datetime.datetime.strptime(str(i.get_due_date()), '%m/%d/%Y')
            # If current entry's date is within current week, then print
            if first_week <= entry_date <= last_week:
                # If current entry's due_date does not equal to previous entry, then output the date
                if temp_date != i.get_due_date():
                    print "\nDATE: " + str(i.get_due_date()) + "\n"
                    print i
                else:
                    print i

                temp_date = i.get_due_date()