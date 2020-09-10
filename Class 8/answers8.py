listOne = ["start", "middle", "end"]
for i in range(0, 5):
    for item in listOne:
        print(item)

listTwo = ["start2","middle2", "end2"]
listThree = ["start3", "middle3", "end3"]
listFour = ["start4", "middle4", "end4"]
listFive = ["start5", "middle5", "end5"]

for i in range(0, 5):
    for item in listTwo:
        print(item)

for i in range(0, 5):
    for item in listThree:
        print(item)

for i in range(0, 5):
    for item in listFour:
        print(item)

for i in range(0, 5):
    for item in listFive:
        print(item)

def example(param):
    print(param)
    return True
example("hello") 

def add(a,b):
    return a + b

print(add(7,8))
print(add(9,7)) 
print(add(276, 987)) 

# Question 1 answer
def addlist(listParam):
    total = 0
    for num in listParam:
        total += num
    return total 
print(addlist(1, 2, 3, 4, 5))