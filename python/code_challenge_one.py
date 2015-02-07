###########################################################################################################################################################
# 1. The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.
#
# This is the start of the function to get you started.


def sleep_in(weekday, vacation):
    if weekday and not vacation:
        return False
    else:
        return True


print sleep_in(False, False) # Should return True
print sleep_in(True, False) # Should return False
print sleep_in(False, True) # Should return True
