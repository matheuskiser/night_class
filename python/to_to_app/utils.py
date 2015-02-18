import datetime


class Utils(object):
    
    # Convert argument to a different format. Returns string
    def format_str(self, from_var):
        return from_var.strftime('%m/%d/%Y')

    # Convert argument to datetime format
    def to_date_format(self, from_var):
        return datetime.datetime.strptime(str(from_var), '%m/%d/%Y')
