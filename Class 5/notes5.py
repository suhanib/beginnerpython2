# CLASS 5: STRINGS AND CASTING

"""
we're going to be going in a little more detail about strings today, so let's recall the definition of a string first:
- a collection of alphabets or characters
- character: umbrella term for letters, numbers, or symbols
- strings are usually used to represent words, letters, or sentences
- denoted with single or double quotes
- when you start a string, you have to end it
"""

# STRING OPERATIONS
"""
we went over a lot of basic math operations with numbers that you can do, but there's also some operations that you could do with strings
you can "add" strings
this is called concatenating
"adding" strings is just really mashing them together
"""
print("hello" + "world")
name = "priya"
print("hello name what's up")
print("hello " + name + " what's up")

greeting = "hello " + name + " what's up"
print(greeting)

"""
there's also the use of the multiplication sign * with strings
if you wanted a word printed out multiple times in one string, this is when you could use it
"""
word = "love "
print("i " + word * 3 + "ice cream")

# TRY IT ON YOUR OWN!
"""
first i want you to print out a concatenated string with the value of a variable in the middle
then i want you to assign a variable a concatenated string
then i want you to use multiplication with strings
put in the chat when you're done / if you have questions
"""

string = "word"
print("this is a " + string)

sentence = "this is a sentence, not a " + string
print(sentence)

word2 = "fun "
print("summer " + word2 * 3)

# CASTING
"""
what if we tried to concatenate a string and a number?
"""
price = 12
print("this item is " + str(price) + " dollars")
price += 2
"""
this is the error that you get:
TypeError: can only concatenate str (not "int") to str
you can only concatenate strings together not integers and strings

casting
it's changing the data type of something to something else
you want to change the data type of the variable price so that you can concatenate it with other strings
built-in function to change the data type from something to something else
str()
int()
float()

if you cast a float to an integer, it's going to chop off the decimal it's going to truncate
"""
# TRY IT OUT ON YOUR OWN
example = "13.75"
"""
1. cast this to an integer and print it out
2. cast this to a float and print that out
put in the chat when you're done
"""
print(int(float(example)))

# STRING METHODS
test = "chair343"

# return booleans
print(test.isalpha())
print(test.isdigit())
print(test.isupper())
print(test.islower())
print(test.endswith("r"))
print(test.startswith("c"))

# methods that return a changed string in some way
print(test.upper())
print("HELLO".lower())
print("    hello    ".strip())
print("this is a sentence".split())