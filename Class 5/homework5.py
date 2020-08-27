# CLASS 5 HOMEWORK
# put your answers in answers5.py, save the file, commit it to your branch, and then push the changes
# i'll be checking and making comments on your homework, so make sure you get it done! :)

# QUESTION 1: fix all the errors in the following print statement so that it prints what i want.
print("my favorite number is " + str(343) + " bc it is " + str(int(7.0)) + " cubed. i also like " + str(8*8))
# what it SHOULD print: my favorite number is 343 bc it is 7 cubed. i also like 64.

# QUESTION 2: remove all "a"s from this string to reveal the hidden word.
# hint: take a look at the Python documentation which has some more string methods we didn't go over!
# https://docs.python.org/2.5/lib/string-methods.html
string = "aasaAauAaamaAmaAAaaeaaAAAraaaa"
string = string.lower()
string = string.replace("a", "")
print(string)

# QUESTION 3: evaluate someone's password!
"""
it's a good password if:
- it's not all letters or all numbers
- it's not all lowercase
make a password variable and print out whether it's a good password or not.
test it with different values for the password variable.
"""
password = "asDfGhjkl12345"

if (password.isalpha() or password.isdigit()):
    print("not secure")
elif (password.islower()):
    print("not secure")
else:
    print("secure password!")