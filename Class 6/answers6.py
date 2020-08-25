"""
fruitsList = ["apples", "bananas", "pineapples", "pears", "grapes" ]
print(fruitsList)

print(fruitsList[3])
print(fruitsList[0:3])


fruitsList[3] = "guavas"
fruitsList.append("strawberries")
print(fruitsList)

fruitsList.pop(1)
print(fruitsList)

fruitsList.insert(1, "bananas")
print(fruitsList)

fruitsList.remove("bananas")
print(fruitsList)

fruitsList.insert(1, "bananas")
print(fruitsList)

del fruitsList[1]
print(fruitsList)

fruitsList.insert(1, "bananas")
print(fruitsList)

"""
#1
listOne = ["i", "am", "a", "sentence"]
print(listOne[0])
print(listOne[1])
print(listOne[2])
print(listOne[3])


#2

listTwo = [4,3,6,10,32,86]
var1 = len(listTwo)
print(sum(listTwo[0:var1]))


#3

string = "helloiamastring"
list1 = list()

for letter in string:
    list1.append(letter)
print(list1)

#4
listThree = ["apple", "hello", "awesome", "ew", "bad", "nice", "ant", "abcajdskfl"]
listNew = list()
for word in listThree:
    if word[0] == "a":
        listNew.append(word)
print(listNew)