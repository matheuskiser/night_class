state = raw_input("Which state? ")
idnumber = raw_input("What is your ID Number? ")
expiration = raw_input("Expiration date ")
dob = raw_input("Date of birth? ")
lname = raw_input("Last name? ")
fname = raw_input("First name? ")
address = raw_input("What is your address? ")
city = raw_input("What is your city? ")
zipaddr = raw_input("What is your zip? ")

print "***********************************"
print "Driver's License"
print state
print idnumber
print "DOB: %s" % dob
print "Expiration Date: %s" % expiration
print lname + ", " + fname
print address
print city + ", " + state + " " + zipaddr
print "***********************************"