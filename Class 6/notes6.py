# CLASS 6: LISTS

# WHAT IS A LIST?
"""
so let's start by thinking about what a list is in real life
one really common list that i think we've all made or seen being made is a grocery lisst
in it's very traditional form, you would take a pieced of lined paper, and on each line, you write a different item that you need from the store
so you have a bunch of stuff in your list, but it's all on one piece of paper
and if you have to access a specific item in your list, all you have to do is go to that specific line that you wrote it on

a list in code works the same way
just like you have a bunch of stuff in your grocery list but they're all on one piece of paper, a list in code is a collection of info
that's all stored under one variable
formal definition: a list is a data type that stores a collection of information under one variable name
"""

# HOW TO MAKE A LIST
"""
so how do you make a list? you need:
    the name of your list
    an equal sign to assign the value to the variable
    square brackets
    the information you want to store in your list, withing the square brackets
"""
groceryList = ["onions", "ice cream", "apples", "salad", "carrots"]
"""
you use commas to separate every item in your list
above i've made our grocery list and i put 5 strings in the list
you can put anything in a list: strings, booleans, ints, floats, even other lists
you can also mix data types in your list (have both ints and strings in a list for example)
"""
# TAKE A MINUTE and make your OWN LIST!

# HOW TO SEE WHAT'S IN A LIST
"""
if you wanted to print out the whole list, you could just use a print statement with the list name
print(listName)
what this will do is actually print out everything - including the brackets, quotes, commas etc
"""
print(groceryList)
"""
what if you wanted to access only a specific item in the list? you can use something called the index
remember the physical grocery list that we were talking about at the beginning 
we wrote every item in the list on a different line, and to access that item we would go to its line
index is the same way
an index is the position of an element in the list
indexes in code start with 0
the first element in a list has an index of 0
the second element in a list has an index of 1
the third element in a list has an index of 2

KEY: the index is just what position an item is at in the order of the list, and it starts with 0 and then increases by 1 each time
index   |  0        |   1       |   2       |    3      |   4 
item    | "onions"  |"ice cream"| "apples"  |  "salad"  | "carrots"

to get the element of a list at a certain index, all you have to do is listName[index]
you can also use indexes to access a subsection of the list or a range
listName[startingIndex:endingIndex] the endingIndex is not included
"""
print(groceryList[1])
print(groceryList[1:3])
# TRY IT OUT! print out the 4th element in your list, and print out a subsection of your list from index 0 to 3

# CHANGING WHAT'S IN A LIST
"""
if you want to change one of the values that is already stored in a list, you can use the index to do this
say i don't the carrots i'm going to change it to oranges
listName[index] = "new value"
"""
groceryList[4] = "oranges"
print(groceryList)
"""
what happens when you try to access an index that is not included?
what if i try to do listName[5]
you get an error that says IndexError: list index out of range
so what this means is that the index that you are trying to access does not yet exist
lists in python do not have a set length, so it is possible to add to them
however, you can't do it by using index notation with an index that does not yet exist
groceryList[5]

ADDING TO A LIST
you cannot use an index to add to a list
but you can use a built-in function called .append()
let's break down what this is
it's a piece of code built-in to python to work with lists
you can use however many times you want
it takes a parameter, which is a piece of information that helps it do what it needs to do
the parameter in this case is what you want to add to your list
the way you use it is by calling it with your list and the dot operator
listName.append("what you want to add")
"""
groceryList.append("strawberries")
print(groceryList)
# TRY IT ON YOUR OWN: try changing index 3 of your list to something else; then try adding something new to your list
"""
continuing on with adding
.append() will always to the end
if you want to put something at a certain index there is another method for that called .insert()
.insert(index, "item that you want to add")
"""
groceryList.insert(2, "granola bar")
print(groceryList)
"""
DELETING
there's actually 3 different ways to delete things from a list
the first one is the del keyword
    - get rid of a specific item: del listName[index]
    - get rid of a range of items: del listName[startingIndex:endingIndex]
    - get rid of the whole list: del listName
the next way to delete is to use .pop()
    - another built-in function like .append()
    - you can put in an index to remove the item at that index
    - if you don't give an index it will just remove the last element
    - .pop() also gives back to you the value of the item it deleted so you can print that out if you want
    - print(listName.pop(index)) will print the value that you just removed
the third way you can delete is using .remove()
    - .remove() is again another built-in function like .append() and .pop()
    - .remove() removes by value
    - so you put in not an index but the value of an item in the list and it will remove it
    - listName.remove("item")
"""
# TRY IT OUT: try deleting something using the del keyword, .pop(), and .remove()

# LENGTH OF A LIST
"""
how can you find out how long a list is if you don't know the last index
there's another built-in function called len()
len(listName) it will tell you how many items are in a list
"""

# STRINGS
"""
you can think of strings as a list of characters
so the same way that you access 1 item in a list, you can use indexes to access 1 character in a string as well
"""
groceryList[2]
string = "suhani"
print(string[2]) # "h" which is the third letter