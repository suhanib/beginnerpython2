# CLASS 7: DICTIONARIES

# INTRO
"""
remember when last week we were first talking about lists, and i gave you the example of real life list: a grocery list
with a list, we were able to store what items we wanted from the grocery store, but not how many of each item we needed
in real life, when making a grocery list, it's very useful to know how much of each item is required
with this setup in a real life grocery list, each line has a pair of information: it has what item we want, as well as how many we need
how would we store a pair of information with lists?
one idea is to have two lists, one for the amounts and one for the items
another idea is to have one list that stores the item then the amount as alternating elements
neither of them are very good ideas
    neither of the options make it explicitly clear that the item and the amount are connected
    it's also hard to manage. if you want to delete or change an item, you have to change it in two places every time so its easy to mess up
is there you know a data structure that can allow you to store paired data effectively?
yes! it's called a dictionary.
"""
items = ["tomato", "potato", "banana", "onion"]
amounts = [3, 5, 4, 6]
groceryList = ["tomato", 3, "potato", 5, "banana", 4, "onion", 6]

# DICTIONARY OVERVIEW
"""
so now that i've set up in very basic terms why we use dictionaries, which is to store paired data, let's give it a more formal definition
and talk about how to set one up
a dictionary is a collection of data that has pairs of "keys" and "values"
so let's actually model that advanced grocery list we were trying to make earlier
"""
groceryDictionary = {"tomato": 3, "potato": 5, "banana": 4, "onion": 6}
"""
i've just created a dictionary.
just like a list, you need a variable name to store all your information under
use the equal sign to assign it the value
you use curly brackets to create a dictionary
then we put in the actual information we want to store in the form of what's called key-value pairs
here, tomato is the key, and 3 is the value
likewise, potato, banana, and onion are keys, and 5, 4, and 6 are their respective values
let's do another example. i take french so i'm going to make a very simple french-english dictionary
"""
frenchToEnglish = {"bonjour": "hello", "merci": "thank you", "au revoir": "goodbye"}
"""
in this example, the french words are the keys, and the english words are the values.
every time you put in a new key-value pair, the key and value are separated by a colon
all the pairs are separated by commas
key-value pairs can be confusing, but it helps if you think of it in terms of an actual dictionary
in a real-life dictionary, the key is the word and the value is the definitino
or for language dictionaries, the key is the word and the value is its translation

so you can see here in my two examples that you're allowed to put in whatever data types you want for your keys and values
you can use ints, floats, booleans, strings, lists, and even other dictionaries
however, it's best practice to keep your keys very simple and short, because you use the keys that you create to access the values

this is getting to one of the biggest differences between lists and dictionaries
besides dictionaries allowing you to effectively store paired data, they also differ in terms of how you access that data
for lists, you use indexes, but for dictionaries you use the keys

dictionaries are unsorted
remember how when you make a list, the information in your list always stays in the order that you put it in
that's because lists are ordered, which means that the order of the items is kept and preserved
this is why indexes work so well for lists. since the elements are in a certain order, it makes sense to access them using a number
that represents the position of the item in the order of the list.
however, dictionaries are not ordered, so the order you put elements in doesn't matter and is not necessarily preserved.
because of that there are no indexes for dictionaries. how could there be if there's no set order?
instead of using indexes you use the keys of the dictionary to access teh values.
"""
print(groceryDictionary["tomato"])
"""
if you notice, it looks really similar to how you access items in a list using an index or even a string
you use the same square brackets to access the value but instead of putting an index within the brackets, you put the key
the value associated with the key "tomato" in this dictionary is 3 so this will print out 3
there's also a built-in method to access values as well .get()
you put the key in parentheses and it will return the value
"""
print(groceryDictionary.get("tomato"))
print(groceryDictionary)
# TRY IT ON YOUR OWN! take the next couple minutes to make your own dictionary and practice accessing and printing out the values
# it's a little hard to think of topics for a dictionary, so here are some ideas:
#   car information (brand, model, year)
#   about yourself (name, age, grade)
#   language dictionary

# DICTIONARY OPERATIONS
"""
now that you have a dictionary, what can you do with it?
well first, we can change the values we've stored
the way we do this is by accessing the value with the key and then assigning it a different value
"""
groceryDictionary["tomato"] = 7
print(groceryDictionary)
"""
you can also add a value
to add, it's just like changing a value except the key you use is the new key
"""
groceryDictionary["eggs"] = 12
print(groceryDictionary)
"""
notice that adding a new key-value pair and changing the value of an existing pair have basically the same syntax
the only difference is what key you provide (an existing one or a new one)
this shows you another important hing about dictionaries: duplicate keys are not allowed
if you try to add a new value to a key that already exists with the intention of having it as a second pair, it will just change
the original value in that spot
this is because keys are used to access info in your dictionary, so if you had two different values for a repeated key, the dictionary
would have no way of knowing which value you wanted to access, which is why repeated keys are simply not allowed
for example, i could not have tomato: 7 and tomato: 3 in the same dictionary

you also can't change a key. if you want to, you have to temporarily store its value somewhere, delete the key, and make a new one, 
and then set it to its old value.
speaking of deleting a key, if you want to delete something you use the del keyword
"""
del groceryDictionary["banana"]
print(groceryDictionary)
# TRY THIS ON YOUR OWN!
# take the next couple minutes to try changing values, adding information, and deleting from the dictionary you created earlier.

"""
want to iterate through a dictionary? easy! you can just use a for-each loop
in this case, the loop variable will take on the value of each key in the dictionary, when you can then use to access the value its paired with
"""
for key in groceryDictionary:
    print(key)
    print(groceryDictionary[key])
"""
want to check if something is in a dictionary? there are a couple ways to do this, depending on whether you're checking for a key or a value
by key:
    use the in syntax: if keyName in dictName
    use the list of keys: dictName.keys() returns a list of all keys in the dictionary that you can then iterate through
by value:
    use the list of value: dictName.values() returns a list of all values in the dictionary that you can then iterate through
"""
if "onion" in groceryDictionary:
    print("onions is on my list!")

for key in groceryDictionary.keys():
    if key == "potato":
        print("i need potatoes")

if "hello" in frenchToEnglish.values():
    print("i can say hello in french")

# TRY IT ON YOUR OWN! take the last 4 minutes to try iterating through a dictionary and printing out eveyr key and value
# as well as searching for certain keys and values in the lit