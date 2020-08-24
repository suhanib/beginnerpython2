name = "anika"
print("hello "+ name + " what's up")

word = "no "
print("i said "+ word * 3 + "to the offer of cleaning the bathroom")

age=13
print(int(float(4.35)))
favoriteNum = 342
reasoning = 7.0**2
alsoLike = 8*8
print("my favorite number is "+ str(342) +" bc it is " +str(int(7.0)) +  " squared. i also like "+ str(8*8))

string = "aasaAauAaamaAmaAAaaeaaAAAraaaa"
string = string.lower()
string = string.replace("a","")
password = "Peanuts123"

print(password.isalpha())
print(password.isdigit())
print(password.isupper())
print(password.islower())

if(password.isalpha() or password.isdigit()):
  print("not secure:(")
elif(password.islower()):
  print("not secure:(")
else:
  print("good password!")


