# CLASS 10: MODULES, PACKAGES, AND LIBRARIES

# MODULES
"""
a module is just a python file that has functions and variables in it
it's just a file that has runnable python code in it
modules are used to break down alrger programs into more manageable and organized units

for example, say you were making a really complex game
so to organize your code, you've already made a bunch of functions
you have a function to:
- move up
- move down
- move right
- move left
- jump
- kick
- block
- punch
- pick up items
- using stuff already in your inventory

imagine having all of those functions in your main runner file
that game file would be so incredibly long, overwhelming, cluttered and slow
instead of keeping all of your functions in this one file, you can make separate files to hold related functions
so for example, you could create one file to manage all of your character movement
it would have functions like move up, down, right, left, jump
then you could create one file to manage all of your fighting actions: kick, block, and punch
your last file could be for all of the quest-related stuff: pick up items and use them
these 3 files would all be called modules

modules are useful in this context because
they help you group together related functions and variables
get rid of clutter in your main file
and they also provide reusibility of your code

benefits of modules in general
besides making programs easier to read and use, there's a lot more that they can give
simplicity
maintainability
reusability

i've just created a module
the way that we use modules is by importing them
import is a key word 

importing the whole module
import and then the module name
the module name is the name of the file but without the .py extension

import modulename
now if you imported it like this and you want to use a function from that file, you have to use the dot . operator
modulename.functionname()

the second way to import is just to import a specific function
this is best for bigger modules
from moduleName import functionName
if you just import one function, you don't need to use the module name
functionname()

the third way to import is to use an alias
from modulename import functionname as alias
import modulename as alias
thats if you want to import it under a different name
"""
from moduleExample import add as a
print(a(3,4))

# PACKAGES
"""
a package is a collection of modules
it also has an initializer file that lets python know that its a package
when would something something like a package be used
say you're working at a big company
each teeam in the company could create a package
each teams package could be used by everyone else
each teams package also contains a module for every person on the team
what's cool about packages is you can actually make packages and upload them to the python package index
this makes your packages avilable for other people to use
what's so powerful about this concept - you can reuse other peoples code and you can make code for other people to use
it means that pythons capabilities are constantly growing and also that you never really have to start completely from scratch
"""

# LIBRARIES
"""
libraries are a collection of packages
the words library, package, and module are sometimes used interchangeably, especially if a package or library has only one module
however, if you are making separate files to import for yourself just locally for your own purposes, that would only be called a module
packages and libraries are external stuff that other people have made

there are some built-in libraries in python that just come available
for built-in libraries, all you need to do is import them
two built-in libraries are math and random
"""
from math import sqrt
sqrt(5)

from random import randint, choice
randint(0,10)
choice(["blue", "orange", "purple"])
"""
but i was also talking about libraries that other people have made
in order for you to use those, you need to install them first and then import them
mac and downloaded python with homebrew: go to your terminal and type brew install packagename
pip install packagename

now go back to your file and say import packagename
"""