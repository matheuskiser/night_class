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

    # Convert argument to a different format. Returns string
    def format_str(self, from_var):
        return datetime.datetime.strptime(str(from_var), "%Y-%m-%d").strftime('%m/%d/%Y')

    # Convert argument to datetime format
    def to_date_format(self, from_var):
        return datetime.datetime.strptime(str(from_var), '%m/%d/%Y')

    def get_today_date(self):
        # Get today's date
        date = datetime.datetime.now().date()
        # Convert date
        now_date_string = self.format_str(date)
        # Convert now_date to datetime
        today_date = self.to_date_format(now_date_string)

        return today_date

    # Returns weekly calendar
    def print_week_calendar(self):
        sorted_dictionary = self.sort_calendar()

        # Returns today's date in date format
        today_date = self.get_today_date()

        # Calculate start and end of current week
        start_week = today_date - datetime.timedelta(today_date.weekday()+1)
        end_week = start_week + datetime.timedelta(6)

        # Convert start and end week dates
        st_week = self.format_str(start_week.date())
        ed_week = self.format_str(end_week.date())

        # Convert start and end week dates to datetime
        first_week = self.to_date_format(st_week)
        last_week = self.to_date_format(ed_week)

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