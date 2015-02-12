class Calendar(object):

    def __init__(self):
        self.calendar_dictionary = []

    def append_entry(self, entry):
        self.calendar_dictionary.append(entry)

    def print_calendar(self):
        temp_date = None

        for i in self.calendar_dictionary:
            if temp_date != i.get_due_date():
                print "\nDATE: " + str(i.get_due_date())
                print i
            else:
                print i
            temp_date = i.get_due_date()