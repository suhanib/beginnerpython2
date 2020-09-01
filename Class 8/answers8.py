# CLASS 8 PRACTICE

def add(num1, num2):
    return num1+num2
print(add(231, 546))
print(add(321, 456))

# CLASS 8 HOMEWORK

# QUESTION 1: write a function that takes in a list of numbers and returns the sum of all the numbers in the list.

def add(listName):
    total = 0
    for num in listName:
        total += num
    return(total)

List = [5, 6, 3, 9]
print(add(List))

# QUESTION 2: write a function that takes in a list of keys and a list of values and returns a dictionary made from those lists.

def dictCombine(dictName, keyList, valueList):
    dictName = {}
    for i in range(0, len(keyList)):
        dictName[keyList[i]] = valueList[i]
    return dictName

Opposite_Colors = {}
colorKey = ["red", "orange", "yellow", "green", "blue", "purple"]
colorValue = ["green", "blue", "purple", "red", "orange", "yellow"]
print(dictCombine(Opposite_Colors, colorKey, colorValue))

# QUESTION 3: write a function that takes in a string and returns how many vowels the string has.

def vowelCount(string):
    return string.count('a') + string.count('e') + string.count('i') + string.count('o') + string.count('u')

print("Your string has" + vowelCount("This sentence has 7 vowels"), "vowels")

# QUESTION 4: write a function to reverse a string.

def reverse(string):
    index = len(string) - 1
    while(index >= 0):
        print(string[index], end = '')
        index -= 1

reverse("Chicken backwards is nekcihC")