# CLASS 3: BASIC MATH and IF STATEMENTS
"""
okay so let's try to do something more than just printing something out. python and any language can do a lot of basic math as well.
i know this doesn't seem very exciting but it's a good place to start with adding more functionality to your prorgams
the operations are pretty self-explanatory; you can use operations in print statements or to assign values to variables
"""
add = 7 + 7
subtract = 7 - 7
multiply = 4 * 2
divide = 15 / 2
integerDivide = 15 // 2
"""
a note about division:
one slash is called float division. so it will give you a decimal answer every time. 15 / 2 = 7.5
two slashes is called integer division. it will give an integer every time. it's not going to round your answer.
it's jsut going to chop off the decimal. that's called truncating.  15 // 2 = 7
"""
power = 7 ** 2
modulo = 14 % 5 # return 4 because the remainder here is 4
"""
what we've written above is all regular operators, they look like you're writing it into your calculator
assignment operators on the other hand are the operator followed by an equal sign
it takes the current value of the variable you're using, does the operation with the following number, and then
reassigns the value back to the variable
"""
add += 4
subtract -= 3
multiply *= 2
divide /= 2
integerDivide //=2
# TRY THIS OUT ON YOUR OWN! make a couple variables, do some operations, and then also use some assignment operators


secret = 0 # secret is 0
secret += 1 # secret is 1
secret -= 5 # secret is -4
secret **= 2 # secret is 16
secret *= 6 # secret is 96
secret %= 10 # secret is 6
print(secret)

# IF STATEMENTS
"""
the next topic we are going to learn about is if statements
they allow you to make decisions in your code
they allow you to choose what happens based on certain conditions
so if a condition that you specify is true, then some other code that you specify will execute (run)
the condition is a statement that evalutates to a boolean

if (condition):
    # write here what you want to happen if the if statement runs
    print("hello")
    print("hello again")

indentation is so important in python
in other languages they have a lot of semicolons and curly brackets and things like that to tell the computer where code blocks start and end
one of the reasons that python is so simple and clean is because it doesn't have that stuff
it relies on the programmer indenting to know where code blocks start and where they end
"""
var = True
if (var):
    print("vasdfghjkl")

num = 7
if (num > 8):
    print("num is greater than 8")
print("hello")
# TRY IT ON YOUR OWN! make a variable for your age; make an if statement that represents if you can watch a PG 13 movie or not
# >= is greater than or equal to

"""
what if you want more options for your if statement?
like what if you wanted something else to happen if your first choice didn't go through?
imagine you're at an ice cream store.
i'm making a "haveCoffee" variable which is a boolean to represent whether the ice cream store i'm at has coffee or not
if they do, i'll get coffee
if they don't, i dont really care what other flavors they have, i'll jsut get vanilla
how do i represent in code what happens if the ice cream store doesn't have coffee?
you can add an else statement
an else statement only happens if the if condition is not true
if the if condition goes through, the else statement will not run

what if you had three possible flavor choices? you can add an an elif (it stands for else if)
"""
haveCoffee = True
haveOrange = True
haveStrawberry = True
if (haveCoffee):
    print("i'll have one scoop of coffee on a cone")
elif (haveOrange):
    print("i'll have one scoop of orange sorbet")
elif (haveStraberry):
    print("straberry")
else:
    print("i'll take a scoop of vanilla :(")

"""
mathematical comparisons can be used for if statements
when you try to compare for equality you need to use 2 equal signs
"""
age = 13
if (age == 13):
    print("i am thirteen")