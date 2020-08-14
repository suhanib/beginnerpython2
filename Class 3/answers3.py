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