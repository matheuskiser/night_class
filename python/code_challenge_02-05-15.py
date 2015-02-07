# Write a function that takes in a person's name, and prints out a greeting.
# The greeting must be at least three lines, and the person's name must be in each line.
# Use your function to greet at least three different people.
# Bonus: Store your three people in a list, and call your function from a for loop.

# Write a function that takes in two numbers, and adds them together. Make your function print out a sentence showing
# the two numbers, and the result.
# Call your function with three different sets of numbers.
# Modify Addition Calculator so that your function returns the sum of the two numbers.
# The printing should happen outside of the function.


def greeting(name):
    print "Hi, " + name
    print name + ", It is great to meet you."
    print name + " is a great name!\n"

names = ['Paul', 'John', 'Ben']

for i in names:
    greeting(i)


def add_numbers(x, y):
    return x + y

numbers = [[1, 2], [3, 4], [5, 6]]

for i in numbers:
    print "Adding numbers " + str(i[0]) + " and " + str(i[1]) + "... The result is = " + str(add_numbers(i[0], i[1]))












