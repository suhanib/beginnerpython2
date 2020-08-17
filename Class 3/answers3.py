# CLASS 3 PRACTICE

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

age = 20

if (age == 13):
    print("This must be your first time watching a PG-13 Movie!")   
elif (age > 13 and age <= 150):
    print ("Welcome to the PG-13 Movie!")
elif (age > 150):
    print("You are too old")
else:
    print("You are too young")

#last name first letter
A = False
B = False
C = False
D = False
E = False
F = False
G = False
H = False
I = False 
J = False
K = False
L = False
M = False
N = False
O = False
P = False
Q = False
R = False
S = False
T = False
U = False
V = True
W = False
X = False
Y = False
Z = False

age = 16
if (age >= 18 and age < 23):
    school = "college"
if (age >= 14 and age < 18):
    school = "high school"
if (age >= 11 and age < 14):
    school = "middle school"
if (age >= 6 and age < 11):
    school = "elementary school"
if (age < 6 or age >= 23):
    print ("You don't go to school")
    school = "X"
elif (A or B or C or D or E or F or G or H or I or J or K or L or M):
    print("You go on Monday and Tuesday to your" , school)
elif (N or O or P or Q or R or S or T or U or V or W or X or Y or Z):
    print("You go on Thursday and Friday to your" , school)

alphabet = "Z" 
if (alphabet < "m"):
    print("hi")
else:
    print("bye")

# CLASS 3 HOMEWORK

# QUESTION 1:
"""
A company decided to give a bonus of 5% to employees who have worked there for more than 5 years.
Write a program that will print out the total amount the employee will earn given their current salary and how many years they have worked.
Test it by changing the value of the years variable from under 5 to over 5.
"""
salary = 90000
years = 4.999999999999999999999999999999
# 16 9's makes it round up to 5. Do you know why its only accurate up to there. Also where do i see your comments

if (years > 5):
    print("You earn", salary * 1.05)
else:
    print("You earn", salary, ". Sorry no bonus this time. You will have to work for", 5 - years, "more years to start earning a bonus.")

# OR

if (years > 5):
    salary *= 1.05
print("You earn", salary)

# First one is more accurate because the salary isn't actualy changed by bonus

# QUESTION 2: 
"""
A school has the following rules for their grading system:
    - above 90: A
    - 80 to 89: B
    - 70 to 79: C
    - 60 to 69: D
    - below 60: F
Create a program that will print out a letter grade based on the value of an integer variable storing a number grade.
Test it by changing the value of the numberGrade variable.
"""
numberGrade = 79


if (numberGrade >= 120):
    print("You must be joking. We don't give that much extra credit")
elif (numberGrade >= 90):
    print("You got an A")
elif (numberGrade >= 80):
    print("You got a B")
elif (numberGrade >= 70):
    print("You got a C")
elif (numberGrade >= 60):
    print("You got a D")
elif (numberGrade >= 0):
    print("You got an F")
elif (numberGrade < 0):
    print("How?")