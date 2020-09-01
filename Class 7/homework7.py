# CLASS 7 HOMEWORK
# put your answers in answers7.py, save the file, commit it to your branch, and then push the changes
# i'll be checking and making comments on your homework, so make sure you get it done! :)

# QUESTION 1: write a program that uses a loop to take a list of keys and a list of values and 
# combine them into a dictionary.
keys = ["name", "age", "grade", "school"]
values = ["suhani", 16, 12, "hths"]
# expected output: personalInfo = {"name":"suhani", "age":16, "grade": 12, "school": "hths"}
personalInfo = {}
for i in range(0, len(keys)):
    personalInfo[keys[i]] = values[i]
print(personalInfo)

# QUESTION 2: write a program that prints all the keys and values of only the unique values in the dictionary.
favoriteColor = {"suhani":"blue", "didi":"pink", "mausam":"red", "priya":"blue", "mom":"red", "dad":"orange", "nina":"purple"}
# expected output: (because blue and red are repeated values)
#   didi pink
#   dad orange
#   nina purple

for key in favoriteColor:
    if (list(favoriteColor.values()).count(favoriteColor[key]) == 1):
        print(key, favoriteColor[key])

# SOME EXTRA LIST QUESTIONS
# QUESTION 3: write a program to get the smallest item in an unsorted list.
listTwo = [13,4,8,2,10]

print(min(listTwo))

smallestNum = listTwo[0]
for num in listTwo:
    if (num < smallestNum):
        smallestNum = num
print(smallestNum)

# QUESTION 4: write a program to make a new list which contains only the unique values 
# in the original one.
listThree = [1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,3,3,4,4,4,5,5,5,5,5,5,5]
# sampleOutput = [1,2,3,4,5]
output = []
for num in listThree:
    if (num not in output):
        output.append(num)
print(output)