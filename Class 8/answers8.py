# Practice
def add(a,b):
    return a + b


# QUESTION 1: write a function that takes in a list of numbers and returns the sum of all the numbers in the list.
def addList(numList): 
    whole = 0
    for indx in range(len(numList)):
        whole += numList[indx]
    return whole 

myList = [7, 6, 8, 1]
print (addList(myList))

# QUESTION 2: write a function that takes in a list of keys and a list of values and returns a dictionary made from those lists.
def makedictionary(keys, values):
    dictionary1 = {}
    for j in range(len(keys)):
        dictionary1[keys[j]] = values[j]
    return dictionary1

list1 = ("name", "fav color")
list2 = ("sara", "pink")
print (makedictionary(list1, list2))


# QUESTION 3: write a function that takes in a string and returns how manyy vowels the string has.
def findVowels(stringParam):
    list3 = stringParam
    vowelCount = 0
    for h in range(len(list3)):
        if ("a" == (list3[h]) or "e" == (list3[h]) or "i" == (list3[h]) or "o" == (list3[h]) or "u" == (list3[h]) ):
            print("i am a vowel")
            vowelCount += 1
        else: 
            print(list3[h])
    return vowelCount

str5 = ("i am a string")   
print(findVowels(str5))


# QUESTION 4: write a function to reverse a string.
def backwards(listname):
    mylist3 =[]
    listLen = len(listname)
    for c in range(listLen): 
        #Two ways to write 
        #mylist3.insert(c, listname[listLen - c - 1])
        mylist3.append(listname[listLen - c - 1])
    return mylist3

string = "hello"
print(backwards(string))


