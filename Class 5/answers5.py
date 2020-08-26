word = "fun"
print("going to the waterpark is " + word)

activity = ("going to the waterpark is " + word)
print(activity)

example= 10.5
print(int(example))
print(float(example))

print("my favorite number is "+ str(343)  + " bc it is " + str(int(7.0)) + " cubed I also like " + str(8*8))

string = "aasaAauAaamaAmaAAaaeaaAAAraaa"
string = string.lower()
string = string.replace("a", "")
print(string)

password = "12345"

if (password.isalpha() or password.isdigit()):
    print("not secure")
elif (password.islower()):
    print("not secure")
else:
    print("secure password")