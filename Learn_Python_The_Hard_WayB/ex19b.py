#Study Drill
def bethel_male_and_female(bethel_male, bethel_female):
	print "We have %d males!" % bethel_male
	print "We have %d females!" % bethel_female
	print "Man that's enough for a large house!"
	print "Get a blanket.\n"
	
print "1) We can just give the function numbers directly:"
bethel_male_and_female(20, 30)

print "2) OR we can use varibles from our script:"
amount_of_males = 10
amount_of_females = 50

bethel_male_and_female(amount_of_males, amount_of_females)

print "3) We can even do math inside too:"
bethel_male_and_female(20 - 10, 30 + 20)

print "4) And we can combine the two, varibles and math:"
bethel_male_and_female(amount_of_males + 10, amount_of_females - 20)

print "5) We can use numbers and variables:"
amount_of_guys = 10 + 05
amount_of_ladies = 50 - 15
bethel_male_and_female(amount_of_guys, amount_of_ladies)

print "6) We can ask users for numbers directly:"
number_of_guys = int(raw_input("Males = "))
number_of_ladies = int(raw_input("Females = "))
bethel_male_and_female(number_of_guys, number_of_ladies)

print "7) We can ask users for variables:"
males = 40
females = 90
raw_input("How do we know the number of males? ")
raw_input("How do we know the number of females? ")
bethel_male_and_female(males, females)






