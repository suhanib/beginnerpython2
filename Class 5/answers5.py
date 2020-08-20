word = "pencil "
print("I hold my " + word + "in my right hand.")

sentence = "My " + "desk " + "is " + "black."
print(sentence)

wordTwo = "very "
print("The sun is " + wordTwo * 3 + "bright." )


example = "13.75"
print(int(float(example)))
print(float(example))


#1
print("my favorite number is " + str(343) + " bc it is " + str(int(7.0)) + " cubed. i also like " + str(8*8))

#2
string = "aasaAauAaamaAmaAAaaeaaAAAraaaa"

print(string)
string = string.lower()
string = string.replace("a","")
print(string)

#3
pwd = str(input("Enter your password (don't worry you won't get hacked): "))

while(pwd.isalpha() or pwd.isdigit() or pwd.islower()):
    
    if(pwd.isalpha()):
        print("Try using both letters and numbers")
    elif(pwd.isdigit()):
        print("Try using both letters and numbers")
    elif(pwd.islower()):
        print("Try using some uppercase letters too")
    pwd = str(input("Enter your password (don't worry you won't get hacked): "))
print("Strong password!")
      