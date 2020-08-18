# CLASS 4 PRACTICE
rainy = True
sunny = True

if (rainy and sunny):
    print("RAINBOW")


age = 12.5
height = 52

if (age > 12 and height >= 50):
    print("you can ride the first roller coaster")
if (age >= 13 or height >= 55):
    print("you can ride the also second roller coaster")
else:
    print("you don't meet the requirments")

if ("0" not in "2000"):
    print("yay this works")
else:
    print("yay 'not in' works")

if ("A" in "Suhani"):
    print("this is not case-sensitive")
else:
    print("this is case sensitive")

for x in range(1, 8):
    print(x)
    print("Xhaiden")

numChips = 10
print("You have 10 chips.")
while (numChips > 0):
    numChips -= 1
    print("Crunch. You have", numChips, "chips left.")
print("That was yummy!")

# CLASS 4 HOMEWORK

# QUESTION 1: sum up all numbers from 1 to a number of your choice
# for example, if i choose 10, then i should print out a sum of 55

n=10
print((n*(n+1))/2)


# QUESTION 2: write a program that finds all numbers which are divisible by both 5 and 7, between 1500 and 2700 (both included)
var = 1505

while (var < 2701):
    print (var)
    var += 35

# QUESTION 3: what's missing in this while loop?
x = 10
while (x > 0):
    print(x)
    x -= 1 # <-- inserted code
print("liftoff!")