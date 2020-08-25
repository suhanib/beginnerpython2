# CLASS 5 PRACTICE

name = "Bobby"

print("Hi there " + name + ". How are you?")

hi = "Hi there " + name + ". How are you?"

print(hi)

print("mew " * 12)

num = "3"

print(int(num))
print(float(num))

mun = "13.75"
print(int(float(mun)))
"""
name = input("What is your name?\n")
if (name[0].islower()):
    print("Capatilize the first letter")
else:
    print("Good job")
"""
    # CLASS 5 HOMEWORK

# QUESTION 1: fix all the errors in the following print statement so that it prints what i want.
# print("my favorite number is" + 343 + "bc it is " + 7.0 + " squared. i also like " + 8*8)
# what it SHOULD print: my favorite number is 343 bc it is 7 squared. i also like 64.

print("my favorite number is " + str(343) + " bc it is " + str(int(7.0)) + " squared. i also like " + str(int(8*8)))

# QUESTION 2: remove all "a"s from this string to reveal the hidden word.
# hint: take a look at the Python documentation which has some more string methods we didn't go over!
# https://docs.python.org/2.5/lib/string-methods.html

string = "aasaAauAaamaAmaAAaaeaaAAAraaaa"
"""
while("A" in string or "a" in string):
    if(string.startswith("a") or string.startswith("A")):
        string = string.lstrip("aA")
    else:
        print(string[0])
        string = string.lstrip(string[0])
"""
string = string.replace("a", "")
string = string.replace("A", "")
print(string)


# QUESTION 3: evaluate someone's password!
"""
it's a good password if:
- it's not all letters or all numbers
- it's not all lowercase
make a password variable and print out whether it's a good password or not.
test it with different values for the password variable.
"""
password = "P8&"

if(password.isdigit()):
    print("You need some letters")
elif(password.isalpha()):
    print("You need some numbers")
elif(password.isupper()):
    print("You need some of your letters to be lowercase")
elif(password.islower()):
    print("You need some of your letters to be uppercase")
else:
    print("Your passwordd is secure")