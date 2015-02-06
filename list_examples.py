# Assign list of careers
careers = ['Developer', 'Cook', 'Server', 'Doctor']

# Finds the index of each item
for i in careers:
    print "Index of " + i + " is: " + str(careers.index(i))

# Checks to see if item is in list
print "Is Developer in the list? "
print 'Developer' in careers
print "Is Cook in the list? "
print 'Cook' in careers
print "Is Server in the list? "
print 'Server' in careers
print "Is Doctor in the list? "
print 'Doctor' in careers

# Append a new career to the list
careers.append('Bar Tender')

# Insert a new career at the beginning of the list
careers.insert(0, 'Accountant')

# Print out list
for i in careers:
    print i