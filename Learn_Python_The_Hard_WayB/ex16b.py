# Study Drill
from sys import argv

script, filename = argv

txt = open(filename)

print "Here is the file %r:" % filename
print txt.read()
txt.close()

print "Let's open the file again"
file_again = raw_input("> ")

txt_again = open(file_again)

print "Here is the file %r:" % txt_again
print txt_again.read()
txt_again.close()
