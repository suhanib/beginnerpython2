
"""
height = 55
age = 12

if(age > 12 and height > 50):
    print("You can ride rollercoaster #1!")
if(age>= 13 or height>=55):
    print("You can ride rollercoaster #2!")


if("ti" in "pratik"):
    print("what's the point of this again?")

for i in range(1, 12):
    print(i)
print("end")

for i in range(1, 8):
    print("Pratik")

chips = 10
while (chips >0):
    chips -= 1
    print("You ate one chip, you now have", chips, "chips")
"""
#Homework


#1
num1 = int(input("Enter an integer: "))
total = 0
for i in range (1, num1 + 1):
    total += i
print(total)

#2 
for i in range (1500, 2701):
    if (i % 5 == 0 and i % 7 == 0):
        print(i)


#3. The missing line is x -= 1