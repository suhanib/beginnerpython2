print(4 + 7)
print("4 + 7")
add = 234 + 684
print(add)
print("add")
print(15 / 7)
print (15 // 7) # division that chops of the end. 8.9 would be truncated to 8
print(7 ** 2) # exponent. This is 7^2
print (14 % 5) # says the remainder
add -= 234
print(add)
modulo = 284 % 5
print(modulo)
modulo %= 3
print(modulo)
modulo -= 101
print(modulo + 100)
modulo -= 90
print(modulo)
modulo //= 7
print(modulo)

modulo = 10

if (modulo < 0):
    print("i am", modulo, "so i am negative")
else:
    print(10)

hi = False
if (hi):
    print("Python is great!")

age = 50

if (age == 13):
    print("This must be your first time watching a PG-13 Movie!")   
elif (age > 13 and age <= 150):
    print ("Welcome to the PG-13 Movie!")
elif (age > 150):
    print("You are too old")
else:
    print("You are too young")

weight = 100
if (weight <= 100 and age >= 13):
    print("You can take a large coke and medium popcorn to the movie.")
elif (weight >=101 and weight <=120 and age >=13):
    print("You can take a small coke and small popcorn.")
else:
    print("No coke, no popcorn.")
