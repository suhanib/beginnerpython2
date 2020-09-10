# CLASS 9: INPUT AND OUTPUT

# INTRO
"""
in this lesson we are going to be learning about how to add a lot of complexity to our programs
we are going to be able to take in information from the user or some external source and also put out stuff for other people to see
this is called input and output
input is what your program takes in
and output is what your program puts out or returns
input --> program --> output
"""

# INPUT() FUNCTION
"""
this is a built-in function that allows you to take input from the user
this is called command-line input because the user has to type in their input in the terminal, which is also called the command line
input() can be used just like print()
the parameter that input takes is the string that you would want printed to the user to inform them of what type of information you are looking for
from them
this parameter is referred to as the prompt
you can thiknk of it as the question that you are expecting the user to answer with their input

name = input("what's your name? ")
print("hello " + name)
age = int(input("how old are you? "))
print("in four years, you will be", age + 4)

this line prints out a string which is the one you specified "what's your name? " and then it allows the user to put in their answer
again you can put in one line of stuff, as soon as you press enter tho the answer is accepted
you currently can't do much with the answer
but we can change that
the simple way to do stuff witht he answer after asking the question is to store it in a variable

1. won't run anything else unless you type in something for the input function answer in the command line
2. only returns strings so you have to cast to an int or float if you want to use it as a number
"""

# TRY IT ON YOUR OWN! ask the user a question using the input function and print out the result
# try taking in a number and casting the result so that you can use it for math

# INTRO TO FILES
"""
what if you wanted to take ni a lot of input
if you were using the input() function for that it would be really annoying
there is a way to do that
it's actually by using separate files to hold the information that we want to input
and it's also possible to use separate files to display output as well
instead of just putting it out to the terminal you can actually output some information to a file that is so much easier to save view and share
what type of file can we use for this type of stuff
we can just text files
they just files that hold some text
.txt
"""

# OPEN FUNCTION
"""
there are three main things that you can do with files in python: read, write, append
before you do any of these things though, you need to open the file
it's just like real life: you can't possibly add to or edit or even see a google doc unles you open it first
in python what you can do with the file is based on how you open it
there's an open function for files and one of the parameters is called a mode
its very simple its a one or two character string but it tells python what you are allowed to do with your file
based on what mode you pass as a parameter to the open function, you can do different things with your file
when you call the open function, you also have to create a variable to represent your file
we will use this variable throughout the program to refer to our file and call other functions on it

full syntax for the open function looks like this
variable = open("filename.txt", "mode")
"""

# READING A FILE
"""
for this to work, your text file has to be in the same folder as your python program
the mode for reading is "r"
"""
f = open("test.txt", "r")
"""
for reading, you have to make sure that the file name that you specify already exists
f is the variable that we are using the refer to the file
= is used to assign the variable to the result of the open function
open function call 
parentheses
first parameter is the file name in quotes
second parameter is the mode, in quotes, separated by a comma from the first parameter

to read a whole file, you would call .read()
to read only one line at a time, you would call the function .readline()
"""
print(f.read())
f.seek(0)
print(f.readline())

"""

is because these functions store the current position they are at in the file
so for example, when we call read(), it reads the whole thing
so this means it starts at the beginning of the file and then goes line by line and prints out until it reaches EOF (end of file)
now after you call .read() the psotioon that it stores in the file is at the end
if you call .readline() its already at the end so theres nothing left to read
so its just prints an empty lien
so the question is how to do you reset what line the position is at in order to keep reading it over again
there is a function for this called .seek()
in its default version this function takes 1 parameter which is the line number that you want to return to, starting with the top line = 0
this resets the position in the file to whatever number you specified

closing the file you have after you're done using it
also if you wanted to open the file in the same program with a different mdoe, you have to close it first
"""
f.close()

# WRITING
"""
writing to the file means editing the contents of the file
we are going to use the open function just like we did for reading except this time with the mode "w"
the mode w lets you write only
if you wanted to read and write you would have to use the mode "w+"
one thing to note is that it completely overwrites what you already had there
everything that was there will be gone and replaced with what we put in as the parameter
"""
f = open("test.txt", "w")
f.write("hello")
f.close()

# APPENDING
"""
this allows you to just add on to the end of a file
it's not going to get rid of all stuff that you already have
so the way that you can append is use the open function with the mode "a"
"""
f = open("test.txt", "a")
f.write("\nline2")
f.close()