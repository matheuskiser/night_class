__author__ = 'matheuskonzeniser'

import math

loose_change = [
    {"denomination":"nickel","year":"2014"},
    {"denomination":"dime","year":"2014"},
    {"denomination":"nickel","year":"2014"},
    {"denomination":"quarter","year":"2014"},
    {"denomination":"nickel","year":"2014"},
    {"denomination":"nickel","year":"2014"},
    {"denomination":"dime","year":"2014"},
    {"denomination":"nickel","year":"2014"},
    {"denomination":"nickel","year":"2014"},
    {"denomination":"dime","year":"2014"},
    {"denomination":"nickel","year":"2014"},
    {"denomination":"quarter","year":"2014"},
    {"denomination":"quarter","year":"2014"},
    {"denomination":"quarter","year":"2014"},
    {"denomination":"quarter","year":"2014"},
    {"denomination":"nickel","year":"2014"},
    {"denomination":"nickel","year":"2014"},
    {"denomination":"dime","year":"2014"},
    {"denomination":"dime","year":"2014"},
    {"denomination":"dime","year":"2014"},
    {"denomination":"dime","year":"2014"},
    {"denomination":"dime","year":"2014"},
    {"denomination":"dime","year":"2014"},
    {"denomination":"dime","year":"2014"},
    {"denomination":"dime","year":"2014"},
    {"denomination":"dime","year":"2014"},
    {"denomination":"dime","year":"2014"},
    {"denomination":"dime","year":"2014"},
    {"denomination":"nickel","year":"2014"},
]

# How many stacks of N units can we make for each denomination of coin?

grouped = {}
key_holder = []
stack_limit = 4

for coin in loose_change:
    denomination = coin["denomination"]

    if not denomination in key_holder:
        key_holder.append(denomination)
        grouped[denomination] = 1
    else:
        grouped[denomination] += 1


for key, val in grouped.items():
    print int(math.ceil(float(val)/float(stack_limit))), "stacks of", key
