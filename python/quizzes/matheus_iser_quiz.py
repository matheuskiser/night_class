__author__ = 'Matheus Konzen Iser'

# Print 'Hello World'
print "Hello World"

# 2. Create a list called fruit that has Apples, Oranges and Bananas as values.
fruits = ['Apples', 'Oranges', 'Bananas']

# 3. Print the list.
for i in fruits:
    print i

# 4. Change Oranges to Grapes using the numeric list index.
fruits[1] = "Grapes"

# 5. Create a loop that prints out each item in the fruit list.
for i in fruits:
    print i

# 6. Create a dictionary called people that has another dictionary for each Bob (age 22), Carol (age 47) and Justin (age 14) with their name and age.
people = {'Bob': {'Name': 'Bob', 'Age': 22}, 'Carol': {'Name': 'Carol', 'Age': 47}, 'Justin': {'Name': 'Justin', 'Age': 14}}

for i in people.values():
    print "Name: " + i['Name'] + ", Age: " + str(i['Age'])


# 7. Create a function that takes two numbers (a and b) and prints the total value when they are added.
def add(a, b):
    print a + b

# 8. Call your function with 5 and 5, 10 and 15 and 3 and 6.
add(5, 5)
add(10, 15)
add(3, 6)


# 9. Create a function that takes user input of an integer and loops through printing that number plus 5 until it reaches 1000.
def user_input(num):
    temp_num = num

    while temp_num < 1000:
        print temp_num
        temp_num += 5

num_user = int(raw_input("Enter a number: "))
user_input(num_user)

# 10. Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
num_fiz = 1

while num_fiz <= 100:
    if num_fiz % 3 == 0 and num_fiz % 5 == 0:
        print "FizzBuzz"
    elif num_fiz % 3 == 0:
        print "Fizz"
    elif num_fiz % 5 == 0:
        print "Buzz"
    else:
        print num_fiz

    num_fiz += 1


# 11. Create a class called customer that takes the customer name as a variable and is initialized with age, location of Washington and a credit score of 718.
class Customer(object):

    def __init__(self, name,  age=24, location="Washington", score=718):
        self.name = name
        self.age = age
        self.location = location
        self.credit_score = score


# 12. Create an object from your customer class with the name of Jessie.
customer_object = Customer("Jessie")

# 13. Print the name value of your object.
print customer_object.name

# 14. Print the location of your object.
print customer_object.location

# 15. Print the credit score of your object.
print customer_object.credit_score

# 16. Change the credit score of your object.
customer_object.credit_score = 810

# 17. Print the new credit score of your object.
print customer_object.credit_score
