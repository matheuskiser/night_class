# Assigns a tuple of scores
scores = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Displays the highest and lowest value in the tuple
print "The lowest possible score is " + str(min(scores))
print "The highest possible score is " + str(max(scores))

# Goes through tuple and prints out values
for i in scores:
    if i == 1:
        print "A judge can give a gymnast " + str(i) + " point."
    else:
        print "A judge can give a gymnast " + str(i) + " points."