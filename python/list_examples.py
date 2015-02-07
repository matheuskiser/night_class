# Assign list of careers
careers = ['Developer', 'Cook', 'Server', 'Doctor']

# Assign list of user inputs
user_input = ['Chef', 'Principal', 'Developer', 'Doctor']

# Finds the index of each item
for i in careers:
    print "Index of " + i + " is: " + str(careers.index(i))

# Checks to see if item is in list
print "\n"
for i in user_input:
    print "Is " + i + " in Careers list?"
    print i in careers

# Append a new career to the list
careers.append('Bar Tender')

# Insert a new career at the beginning of the list
careers.insert(0, 'Accountant')

# Print out list
print "\nHere is the full Careers list:"
for i in careers:
    print i