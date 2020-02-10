from sys import argv

script, first, second, third, fourth = argv

age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "Your fourth variable is:", fourth


print "So, you are %r years old, %r tall and %r heavy." % (
age, height, weight)