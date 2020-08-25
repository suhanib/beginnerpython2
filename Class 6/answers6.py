# CLASS 6 PRACTICE
fruitList = ["oranges", "apples", "rasberries", "cantoloupes", "blackberries", "watermelons", "bananas", "grape", "grapefruit",
"mango", "pear", "lychee"]
print(fruitList[3])
print(fruitList[0:3])
fruitList[3] = "dragon fruit"
fruitList.append("rambutan")
print(fruitList)
fruitList.insert(2, "blueberries")
print(fruitList)
del fruitList[5:7]
print(fruitList)
fruitList.remove("apples")
print(fruitList.pop(0))
print(fruitList)

# CLASS 6 HOMEWORK

# QUESTION 1: make a list and print out every item in a list one at a time. do not do print(listName).
listOne = ["i", "am", "a", "sentence"]

for i in range(0, len(listOne)):
    print(listOne[i])

# QUESTION 2: write a program to sum all items in a list
listTwo = [4,3,6,10,32,86]

add = 0
for i in range(0, len(listTwo)):
    add += listTwo[i]
print(add)

# QUESTION 3: convert a string into an actual list, where each element is one character
string = "helloiamastring"
newList = []

for i in range(0, len(string)):
    newList.append(string[i])
print(newList)

# QUESTION 4: go through this list and make a new output list that only contains words from the first list that start with "a". 
listThree = ["apple", "hello", "awesome", "ew", "bad", "nice", "ant"]
listFour = []

for i in range(0, len(listThree)):
    if listThree[i].startswith("a"):
        listFour.append(listThree[i])

print(listFour)