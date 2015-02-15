"""
User picks number n and program returns all prime number from 0 until n.
"""


def is_prime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True


number_picked = int(raw_input("Pick a number: "))

print 2

for i in range(3, number_picked, 2):
    if is_prime(i):
        print i,