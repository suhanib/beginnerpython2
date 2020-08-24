# QUESTION 1: fix all the errors in the following print statement so that it prints what i want.
print("my favorite number is " + "343 " + "bc it is " + "7" + " squared. i also like " + str(8*8) + ".")
# what it SHOULD print: my favorite number is 343 bc it is 7 squared. i also like 64.

# QUESTION 2
string = "aasaAauAaamaAmaAAaaeaaAAAraaaa"
lowercase = string.lower()
answer = lowercase.replace("a","")
print("The hidden word is " + answer + "!!!!") 
# Short form
print("The hidden word is " + string.lower().replace("a","") + "!!!!") 

# QUESTION 3
#password = "3T56vdjjsm"
#password = "ooooooooo"
#password = "33333778"
#password = "3333333jjjjjjjjjjjj"
#password = "Tsasw3333333"

if (not password.islower() and not password.isalpha() and not password.isdigit()):
     print("good password")
else:
    print("bad password")