# CLASS 4: MORE IF STATEMENTS AND LOOPS

# LOGICAL OPERATORS
"""
there are two keywords called boolean or logical operators they can help you make some more complex conditions
the keywords are and & or
they go in between 2 boolean statements
and they return a different boolean
if you use and between 2 booleans, the whole statement will only be true if both sides are true
if you use or between 2 booleans, the whole statement will be true if either side is true

True and True # evaluates to True
True and False # evaluates to False
False and False # evaluates to False

True or True # evaluates to True
True or False # still evaluates to True
"""

num = 30
if (num > 0 or num < 20):
    print(num)

# PRACTICE
"""
you are at six flags
one rollercoaster needs you to be over 12 and 50 inches tall
another rollercoaster needs you to be either at least 13 or at least 55 inches tall

i want you to model both of these rollercoasters using if statements
write an if statement for each rollercoaster make sure it fits the requirements

take 3-ish minutes to do that
and put in the chat when you're done
"""

age = 13
height = 55

# first
if (age > 12 and height > 50):
    print("you can go")
# second
if (age >= 13 or height >= 55):
    print("you can go")

"""
there's also the useful operators not and in
not will change a condition to be the opposite
so if something originally evaluates to False, using not in front of it will make it True

in is a keyword that checks if the left side is in the right side
"""
if (not False):
    print("hello")

if ("a" in "suhani"):
    print("yes")

"""
the last thing about if statements
if you want to compare for equality, then you have to use two equal signs, not one
== compares 
= assigns values
"""

# LOOPS
"""
a loop is a structure that executes code repeatedly until a certain condition is reached
there are 2 main types of loops: for loops and while loops
for loops have a defined start and end, and you know how many times it will run
while loops just keep running until a condition is false and causes it to stop
"""
for i in range(1, 6):
    print("i am in hte loop")

print("after the loop")
"""
this is what a traditional for loop look like
start with the word for
this is the keyword that starts your loop

i is an incrementor or loop variable
it's defined when you make your for loop
it will take on a new value every time you run the loop

in range(1, 6)
it's defining how many values the loop varialbe i will take on 
and also therefore how many times the loop will run
range(1,6) it starts at 1 and goes to 5 it never includes the last value

PRACTICE: what i want you to do is print your name seven times using a for loop
"""

for i in range(1,8):
    print("suhani")

num = 2
while (num < 4):
    print(num)
    num += 1

"""
imagine you have a bag of chips
you want to keep eating it until it's empty
make a while loop that will keep printing out "ate one chip" until you have no more chips
"""
chips = 10
while (chips > 0):
    chips -= 1
    print("ate one chip")
print("bag is empty")