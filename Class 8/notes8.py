# CLASS 8: FUNCTIONS

# INTRO
"""
okay so in the past, we've learned about something that lets you repeat a certain action: loops
both a for and while loop lets you repeat actions you specify for as many times as you want
so say we want to print out the contents of a list 5 different times. how can we do this with a loop?
we'll it's pretty simple:
"""
listOne = ["start", "middle", "end"]
for i in range(0, 5):
    for item in listOne:
        print(item)
"""
what ive done is create a simple list and what's called a nested for loop
a "nested" loop means that there is one loop inside of another
you can see that the for-each loop ive made is indented underneath the traditional for loop i made, which means that the for-each
loop is part of what will execute every time the traditional or outer for loop runs
each time the outer loops runs, the inner for loop will go through the entire list one by one and print out every time
the inner loop will run to compltetion every time the outer loop runs because only when everything inside the outer loop is complete will the
loop variable move on to the next number

ok but what if i had 5 different lists, and i wanted to print out everything in each list 5 times each
the only way we know how to do that now is to rewrite what we wrote above for listOne for every other list
"""
listTwo = ["start2", "middle2", "end2"]
listThree = ["start3", "middle3", "end3"]
listFour = ["start4", "middle4", "end4"]
listFive = ["start5", "middle5", "end5"]

for i in range(0, 5):
    for item in listTwo:
        print(item)

for i in range(0, 5):
    for item in listThree:
        print(item)

for i in range(0, 5):
    for item in listFour:
        print(item)

for i in range(0, 5):
    for item in listFive:
        print(item)

"""
so it did do what we were asking for
it prints out the contents of 5 different lists, 5 times each
but writing that all out was so time-consuming, it loks ugly, and almost all of this code is repeated
so it definitiely leaves you thinking, isn't there a better more efficient way to do this
if you look at the code the only thing that changes every time is what list we're using, literally everything else is the same
is there some way where we could write the code that's repeated only once, and be able to use it multiple times with different lists
so we would somehow allowed to put in what we wanted to be used
well we're in luck, because this is what a function allows us to do
"""

# WHAT IS A FUNCTION?
"""
so before i implement a function for the solution to our problem, let me tell you what a function is exactly
a fucntion is a defined, separate piece of code written to carry out a specific task
a function performs 1 job only; all of the code inside a function is related to only that one job
you can then use that code in the function as many times as you want without retyping it at all by what's called "calling the function"
so let me write a qucik function example to talk about how to create one and all its parts
"""

# ANATOMY OF A FUNCTION
def example(param):
    print(param)
    return True

# function call
example("hello")

"""
1. the def keyword: def is a keyword that stands for "define." any time you make a function, you have to start it with the keyword def.
this lets python know that this is a function. when you create a function, it's said that you are "defining" the function, so it's fitting
that def is the keyword you use.
2. the function name: you can give the function any name you want except for reserved keywords. here i've named my function example.
the function name comes right after the def keyword.
3. parentheses: you need a set of parentheses after a function name, always.
4. parameter: a parameter is the input that the function takes. when you define a function, you treat the parameter as a vriable. so
i can give the parameter any name i want, just like a variable, then use that to refer to that input throughout the function.
when you finally actually use the function, which i will tlka about later how to do, you pass in the real values that you want used.
these real values will replace wherever you used the paramaeter variable name when you defined you function
you would put any parameters that you wnat your function to accept inside the parentheses
a function does not have to have parameters. if you want more than 1, you would separate them with commas.
5. colon: you need a colon after the parentheses
6. function body: this is where you put what you actually want the function to do. it's the code that will execute every time you
use the function. in this case, the function body is what's indented (the print and return)
7. return: the return statement is a special part of the function body. it's the last thing to happen in a funciton, and it will send back a
value that you want to the place that you called the function from. you don't have to return anything, but if you do, it can be anything
like a int boolean list dictionary float string etc
8. function call: you see underneath the function i wrote example("hello"), this is what's called a function call
it's referred to as calling the function, this is how you actually use the function. you write the function name and a set of parentheses
and if there are any parameters you would put those in the parentheses. normally, when you run a program, code executes from top to bottom
it will continue doing this unless you do somethign to change that. so here, because we have a function call, when python sees this call,
it's going to stop executing form top to bottom, go to the function, run that chunk, replace the function call with whatever was return if ther
was something returned, and then once that is done continue executing the rest of the program
a function will not do anything unless its called

the reason that you cannot see what was returned is because we didnt do anyhting with it
the fucntion call right now is on its own
we are not currently doing anything with what it will return
when we ran this, we couldn't see the return value
once the function executes, you can think of the return statement sending something back to the exact same spot where the function was called
function calls can be thought of as placeholders for the value that function will return once its finished in case you want to do something with that
right now we can print it out
since this function that we wrote returns a boolean we can also use that in an if statmeent
"""
print(example("second"))
if(example("third")):
    print("returned true")

# WHY IS THIS USEFUL?
"""
functions are used to bundle a set of instructions that you want to use repeatedly or that, because of their complexity, are
better off self-contianed in a sub-program that you can just ca;ll when needed
because a function doesn't do anything unless it's called but they can also be called and passed whatever you want whenever you want, 
they are a great way to organize your code into related sub-sections that you can then use throughout your program
also, if you had to change how one of your tasks work, it's really to do so when the code is written once, all in one place
"""

# SOLVING OUR EXAMPLE PROBLEM
"""
if you remember the code that was being repeated, it looked like this:

for i in range(0, 5):
    for item in listOne:
        print(item)

what we can do to simplify that a lot is put this in a function
that way we can send a different list as a parameter every time we call the function
so we don't need to rewrite this block every time we need to use a different lsit
"""
def printList(listParam):
    for i in range(0, 5):
        for item in listParam:
            print(item)

printList(listOne)
printList(listTwo)
printList(listThree)
printList(listFour)
printList(listFive)

# TRY IT ON YOUR OWN!
"""
take the next couple minutes to make your own function
i want you to create a function to add two numbers; name the function add
it should take in two parameters that represent the two different numbers
it should return the sum of those two numbers
call the funciton with many different combinations of numbers and print out the results to see if it works
"""
def add(a,b):
    return a + b

print(add(3,4))
print(add(6,5))
print(add(100, 46))
