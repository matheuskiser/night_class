class CalendarEntry(object):
    def __init__(self, title, description, due_date):
        self.entry_title = title
        self.entry_description = description
        self.entry_due_date = due_date

    def __str__(self):
        return "\tTitle: " + self.entry_title + "\n\tDescription: " + self.entry_description + "\n"

    def get_due_date(self):
        return self.entry_due_date