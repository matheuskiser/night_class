chosen_number = 3
guessed = True

while guessed:
	number = raw_input("Guess a number between 0 and 10: ")

	num = int(number)

	if num == chosen_number:
		print "You guessed the number!"
		guessed = False
	elif num < chosen_number:
		print "Your number is less than the number to be guessed."
	elif num > chosen_number:
		print "Your number is bigger than the number to be guessed."
	else:
		print "Invalid Input"