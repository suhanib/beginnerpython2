# and & or are logical operators
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
