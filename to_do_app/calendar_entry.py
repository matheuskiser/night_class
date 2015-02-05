class CalendarEntry(object):
    def __init__(self, title, description, date, time_of_day):
        self.entry_title = title
        self.entry_description = description
        self.date = date
        self.entry_time_of_day = time_of_day

    def __str__(self):
        return "\nTitle: {}\nDescription: {}\nDate: {}\nTime of day: {}\n".format(self.entry_title,
                                                                                  self.entry_description,
                                                                                  self.date,
                                                                                  self.entry_time_of_day)
