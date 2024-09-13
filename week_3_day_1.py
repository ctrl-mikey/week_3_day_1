# # Week3
# # This week we will work on :
# # Working With Strings


# # 1.   Working With Numbers
# # 2.   Getting Input From Users




# # 1.   Building a Basic Calculator
# # 2.   Mad Libs Game

# # Review
# create variables for the following :
# 1. age
,age=16
# 2. name
,name="mikey"
# 3. song
,song="Need4Speed"
# 4. food
,food="chicken"
# 5. number
,number=17
# #now include the variables you just made print in the following...
# Once upon a time, there was a [age] old coder named [name].
print ("Once upon a time, there was a" + age, "year old coder named" + name)
# [name] liked to hum the song [song] while coding. It was so annoying that their teammates would throw [food] until [name] would stop singing.
print (name +"liked to hum the song" + song + "while coding. It was so annoying that their teammates would throw" + food, "until" + name +"would stop singing.")
# Still, [name] was the best coder on the team and could write [number] lines of code every day. Maybe [song] was [name]’s secret power?
print( "Still," + name "was the best coder on the team and could write" + number + "lines of code every day." "Maybe" + song + "was" + name"’s" secret power?)
##########################################################################################
#########################################################################################



##########################################################################################
# The names you use when creating these labels need to follow a few rules:
# 1. Names can not start with a number.
# 2. There can be no spaces in the name, use _ instead.
# 3. Can't use any of these symbols :'",<>/?|\()!@#$%^&*~-+
# 4. It's considered best practice (PEP8) that names are lowercase.
# 5. Avoid using the characters 'l' (lowercase letter el), 'O' (uppercase letter oh),
#    or 'I' (uppercase letter eye) as single character variable names.
# 6. Avoid using words that have special meaning in Python like "list" and "str"


# Here are some exercises to practice the rules:


# Correcting Invalid Names: Below are some invalid names. Correct them according to the rules:


# firstName
# lastName
# email_address
# percentage
# variable_name
# zero
# list_of_names
# Creating Valid Names: Create valid names for the following descriptions:


# The first name of a person
# The last name of a person
# The email address of a person
# The percentage of marks obtained by a student
# A variable to store the number of items in a shopping cart




# Identify Valid and Invalid Names: Identify which of the following names are valid or invalid according to the rules:


# first_name
# lastName
# email_address
# percentage
# variable_name
# variable
# email_address
# percentage%
# illinois



############################################################################################


# # **Working with** **numbers** **bold text**
# We'll learn about the following topics:
# 1. Types of Numbers in Python
# 2. Basic Arithmetic
# 3. Differences between classic division and floor division


# Python has various "types" of numbers (numeric literals).
# 1. We'll mainly focus on integers and floating point numbers.
# Integers are just whole numbers, positive or negative. For example: 2 and -2 are examples of integers.
# 2. Floating point numbers in Python are notable because they have a decimal point in them, or use an exponential (e) to define the number. For example 2.0 and -2.1 are examples of floating point numbers. 4E2 (4 times 10 to the power of 2) is also an example of a floating point number in Python.


##########################################################################################
# #addition
print(2 + 2)
# #multiplication
print(2 * 2)
# #division
print(2 / 2)
# #modulo
print(2 % 2) #remainder
# #powers
print(2 ** 2 )
# #get the max and min of a number
print(max(2,3)) #max number of the two
print(min(2,3)) #min number of the two
# #round a number
print(round(2.5)) #rounds to the nearest 
# # absolute value
print(abs(-2))#absolute value of the number

# # order of operations
print(2 + 10 * 10 +3)# order of operations
# #to do more you need to import special math libraries from python
from math import *    
# #this goes out and grabs some different math functions we can use
# #floor method
print(floor(3.3))
    
# #ceil method
# #sqrt method
print(sqrt(36))
#square root of the number


##########################################################################################
# So what have we learned? We learned some of the basics of numbers in Python. We also learned how to do arithmetic and use Python as a basic calculator. We then wrapped it up with learning about Variable Assignment in Python.
# # **Getting Input from users**
# #how do we get input from users?
# input("what is your name?")
Input("what is your name")
# # basic math calculator
# #ask the user for 2 numbers
print(Give me a number)
print(Give me another number)
# # print out a statement where you:
print("im a school")
# # add them together
print(number1 + number2)
# #multiply
print(number1 ** number2)
# # find the max number
print(number1, number2)
# # find the remainder of the numbers
print(number1 % number2)
# #round one number
print(floor(number1))


##########################################################################################
# # mad libs game
# print("Roses are {color}")
# print("{plural noun} are blue")
# print("I love {celebrity}")
# # On to codehs.com

