# CLASS 7 PRACTICE
Dictionary = {"roloc":"purple", "dessert":"kaju katli", "age":12, "name":"Xhaiden", "number":7}
print(Dictionary.get("purple"))
print(Dictionary["number"])
print(Dictionary)
Dictionary["age"] = 13
del Dictionary["name"]
Dictionary["brothers"] = 2
print(Dictionary)
temporary = Dictionary["roloc"]
del Dictionary["roloc"]
Dictionary["color"] = temporary
print(Dictionary)
print(Dictionary.keys())
print(Dictionary.values())
if ("number" in Dictionary):
    print("numbers is a key in Dictionary")
print("\n\n")

# CLASS 7 HOMEWORK

# QUESTION 1: write a program that uses a loop to take a list of keys and a list of values and combine them into a dictionary.

keys = ["name", "age", "grade", "school"]
values = ["suhani", 16, 12, "hths"]
personalDictionary = {}
index = 0
for key in keys:
    personalDictionary[key] = values[index]
    index += 1
print(personalDictionary)

# QUESTION 2: write a program that prints all the keys and values of only the unique values in the dictionary.

favoriteColor = {"suhani":"blue", "didi":"pink", "mausam":"red", "priya":"blue", "mom":"red", "dad":"orange", "nina":"purple"}
values = []
keys = []
for value in list(favoriteColor.values()):
    if(value not in values):
        values.append(value)
    else:
        values.remove(value)
for key in favoriteColor:
    if(favoriteColor[key] in values):
        keys.append(key)
print("The keys are " + str(keys) + ", and the values are " + str(values) + ".")


# SOME EXTRA LIST QUESTIONS
# QUESTION 3: write a program to get the smallest item in an unsorted list.

listTwo = [13,4,8,2,10]
lowNum = listTwo[0]
for num in listTwo:
    if(num < lowNum):
        lowNum = num
print("The lowest number in the list is " + str(lowNum))


# QUESTION 4: write a program to make a new list which contains only the unique values 
# in the original one.

listThree = [1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,3,3,4,4,4,5,5,5,5,5,5,5]
newList = []
for num in listThree:
    if(num not in newList):
        newList.append(num)
print(newList)