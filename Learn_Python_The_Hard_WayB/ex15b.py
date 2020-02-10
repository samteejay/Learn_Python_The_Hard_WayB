#Study Drill
#Get argument module from the package
from sys import argv

#argv is unpacked and assigned two variables
script, filename = argv

#Open the file and assign to txt
txt = open(filename)

print "Here's your file %r:" % filename
#Read the text file with no parameters
print txt.read()
txt.close()

print "Type the filename again:"
#Recieve the file from the user using keyboard
file_again = raw_input('> ')

#Open the file and assign to txt_again
txt_again = open(file_again)

#Read the text file with no parameters
print txt_again.read()
txt.close()