"""
add = 4+3
print(add) # 7
add += 2
print(add) # 9

mod = 5 % 2
print(mod) # 1

subtract = 34 - 17
print(subtract) # 17
subtract -= 17  
print (subtract) # 0

multiply = 9*9
print (multiply) # 81
multiply **= 1/2
print(multiply) # 9


num1 = int(input("Enter a number: "))
if (num1 % 2 == 1): 
    print("Your integer is Odd")
else:
    print("Your integer is Even")


age = int(input("Enter your age: "))
if(age >= 13):
    print("You can watch PG-13 movies!")
else:
    print("Sorry, you can't watch PG-13 movies.")
"""
# HW
salary = 6000
years = 6
if(years > 5 ):
    salary *= 1.05
print(salary,"dollars")

numberGrade = 73
if(numberGrade >= 90):
    print("A")
elif(80 <= numberGrade <= 90):
    print("B")
elif( 70 <= numberGrade <= 79):
    print("C")
elif( 60 <= numberGrade <= 69):
    print("D")
else:
    print("F")
    