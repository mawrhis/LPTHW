#ex1.py
#------------------------------------
# prints the "string"
print "Hello World"

#ex3.py
#------------------------------------
#prints the string and counts basic math
print "Hens", 25.05 + 30.08 / 6.08
print "roosters", 100 - 25 * 3 % 4
print "Is it less or equal?", 5 <= -2

#result of this is 1.75
print 7.0 / 4.0
#result of this is 1
print 7 / 4

#ex4.py
#------------------------------------
#variables, math with variables
cars = 100
drivers = 30
cars_not_driven = cars - drivers
print "there are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "there will be", cars_not_driven, "epty cars today."

#ex5.py
#------------------------------------
#The %s token allows me to insert (and potentially format) a string. Notice that the %s token is replaced by whatever I pass to the string after the % symbol.
my_name = 'Zed A. Shaw'
my_eyes = 'Blue'
my_hair ='Brown'
# for numbers use %d
my_weight = 180
print "Let's talk about %s." % my_name
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "He's %d pounds heavy." % my_weight

#ex7.py
#------------------------------------
#multiplying of a string
print "." * 10 

#ex8.py
#------------------------------------
formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
#You should use %s and only use %r for getting debugging information about something. The %r will give you the "raw programmer's" version of variable, also known as the "representation."

#ex9.py
#------------------------------------
# \n puts part of the string t a new line
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
print "Here are the months: ", months
# triple """ allows to create a string that spans through multiple lines

#ex10.py
#------------------------------------
# \\ inserts backslash
# \t adds a tab

#ex11.py
#------------------------------------
# raw input - promt user for input
print "How old are you?",
age = raw_input()
print "So, you're %r old" % age

#ex12.py
#------------------------------------
# raw input - promt user for input
age = raw_input("How old are you? ")
print "So, you're %r old" % age

#ex13.py
#------------------------------------
# arguments
from sys import argv # importing argument variable, This variable holds the arguments 
				     # you pass to your Python script when you run it
				     # these things you can import are called modules

script, first, second, third = argv # This "unpacks" argv so that, rather than holding all 
								    # the arguments, it gets assigned to four variables 
								    # you can work with: script, first, second, and third. 
								    # This may look strange, but "unpack" is probably 
								    # the best word to describe what it does. It just says, 
								    # "Take whatever is in argv, unpack it, and assign it 
								    # to all of these variables on the left in order."

print "The script is called:", script #name of the script (.py file)
print "Your fitst variable is:", first #first variable created from argument you type in
print "Your second variable is:", second #second
print "Your third variable is:", third #third

#ex15.py
#------------------------------------
# opens file
from sys import argv 
script, filename = argv
txt = open(filename)
print "Here's your file %r:" % filename
print txt.read()

#ex16.py
#------------------------------------
# opens file
target = open(filename, 'w') # opens fiel for writing
target.truncate() # clears file
#writes line + empty line into file
line1 = raw_input("line 1: ")
target.write(line1)
target.write("\n")
# close file
target.close()

#ex17.py
#------------------------------------
# copy from file to file
from sys import argv
from os.path import exists
script, from_file, to_file = argv
# length of the file
print "The input file is %d bytes long" % len(indata)
# checks if the output file exists
print "Does theoutputfile exist? %r" % exists(to_file)

#ex18.py
#------------------------------------
# functions
#this one is like your scripts with argv
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)
# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)
# this just takes one argument\
def print_one(arg1):
	print "arg1: %r" % arg1
#this one takes no arguments
def print_none():
	print "I got nothin'."

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()

